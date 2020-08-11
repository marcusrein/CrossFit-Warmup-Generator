from flask import render_template, request, url_for, redirect, flash, abort
from appfolder import app, db, bcrypt, mail
from appfolder.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from appfolder.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message

from appfolder.barbell_warmups import *
from appfolder.checks import *
from appfolder.droms import *
from appfolder.exercises import *
from appfolder.getters import *
from appfolder.gymnastics_warmups import *
from appfolder.kb_warmups import *
from appfolder.media import *
from appfolder.metcons import *


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = save_picture(form.picture.data)

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')



@app.route('/yourgear')
def your_gear():
    posts = Post.query.all()
    return render_template('your_gear.html', posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply.warmupgenerator@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    alphabetical_exercises_dict = OrderedDict(sorted(exercises_dict.items(), key=lambda x: x[0]))
    exercise_keys = alphabetical_exercises_dict.keys()

    metcon_time = 'metcon_time'
    drom_time = 'drom_time'

    warmup_duration_selection = ''
    warmup_equipment = []


    if request.method == 'POST':
        # INPUT
        easy_exercises = request.form.getlist('easy_exercises_form')
        easy_exercises = [easy_exercise.lower() for easy_exercise in easy_exercises]
        tough_exercises = request.form.getlist('tough_exercises_form')
        tough_exercises = [tough_exercise.lower() for tough_exercise in tough_exercises]
        warmup_duration_selection = request.form['option']
        warmup_duration_short = 'on' if warmup_duration_selection == 'short' else False
        warmup_duration_long = 'on' if warmup_duration_selection == 'long' else False

        if request.form.getlist('gearcheck1'):
            gearcheck1 = 'on'
            warmup_equipment.append('loop resistance band')
        else:
            gearcheck1 = False
        if request.form.getlist('gearcheck2'):
            gearcheck2 = 'on'
            warmup_equipment.append('pvc pipe')
        else:
            gearcheck2= False

        # TODAYSWOD

        todays_wod = easy_exercises + tough_exercises
        error_message = check_no_input_todays_wod(todays_wod)

        # METCON SELECTION

        metcon_warmup = {}
        metcons_compiled = get_movements_compiled(
            todays_wod, tough_exercises, metcons, metcon_time)
        selected_metcon = metcons_compiled.get('SELECTED MOVEMENTS: ')
        metcon_reps = get_reps(selected_metcon, tough_exercises, metcons)
        metcon_images = get_images_for_display(selected_metcon, metcons)
        for idx, item in enumerate(selected_metcon):
            metcon_warmup[selected_metcon[idx]] = {'img': (metcon_images[idx]),
                                                   'reps': (metcon_reps[idx])}
        # DROM SELECTION

        ## I NEED TO FIND WHY "BANDED SIDE STEPS" or other banded things keep going into drom_warmup despite the dict
        # beiing created _droms_dict_equipment_considered. Thats causing the error in my DROM img list, reps, etc

        droms_dict_equipment_considered = get_new_drom_dict_considering_equipment(warmup_equipment, droms_dict)

        drom_warmup_initial = get_initial_drom_compiled(todays_wod, tough_exercises, droms_dict_equipment_considered, drom_time, warmup_equipment)

        drom_warmup = get_droms_compiled(todays_wod, tough_exercises, drom_time, selected_metcon, warmup_duration_short,
                                         warmup_duration_long, droms_dict_equipment_considered, warmup_equipment)
        print('XXxXXXRXRXRXRXR%%%%%%%%%%%%%%%%%%xxxxx')
        print(drom_warmup)
        print_for_debug = get_movements_compiled(todays_wod, tough_exercises, droms_dict_equipment_considered, drom_time)
        # KEY CODING TO COMBINE MULTIPLE LISTS INTO A SINGLE DICTIONARY  #

        drom_final_dict = {}
        drom_img_list = get_images_for_display(drom_warmup[0], droms_dict_equipment_considered)
        drom_reps = get_reps(drom_warmup[0], tough_exercises, droms_dict_equipment_considered)
        drom_url = get_url_for_display(drom_warmup[0], droms_dict_equipment_considered)
        drom_counter = ['1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ', '10. ', '11. ', '12. ']

        for idx, item in enumerate(drom_img_list):
            drom_final_dict[drom_warmup[0][idx]] = {'img': (drom_img_list[idx]),
                                                    'reps': (drom_reps[idx]),
                                                    'url': (drom_url[idx]),
                                                    'counter': (drom_counter[idx])
                                                    }
        what_droms_warms_up_list = get_why_drom_selected_dict(drom_final_dict, todays_wod)
        drom_final_dict = add_why_drom_selected_to_drom_final_dict(drom_final_dict, what_droms_warms_up_list)

        # GYMNASTICS SELECTION
        tough_gymnastics_movements_from_todays_wod = get_which_movements_are_tough_gymnastics_movements(todays_wod)
        tough_gymnastics_warmups = get_gymnastics_warmup(todays_wod)

        gymnastics_final_dict = {}

        for k, v in gymnastics_warmups.items():
            for tough_gymnastics_movement in tough_gymnastics_warmups:
                if tough_gymnastics_movement == k:
                    gymnastics_final_dict[k] = v

        # KB SELECTION
        kb_warmup = {}

        kb_movements_from_todays_wod = get_which_movements_are_kb_movements(todays_wod)
        kb_warmup_movements_list = get_kettlebell_warmup(todays_wod)
        kb_warmup_img_list = get_images_for_display(kb_warmup_movements_list, kb_warmups_dict)
        kb_warmup_url_list = get_url_for_display(kb_warmup_movements_list, kb_warmups_dict)
        kb_warmup_reps_list = get_reps(kb_warmup_movements_list, tough_exercises, kb_warmups_dict)
        for idx, item in enumerate(kb_warmup_movements_list):
            kb_warmup[kb_warmup_movements_list[idx]] = {'img': (kb_warmup_img_list[idx]),
                                                        'url': (kb_warmup_url_list[idx]),
                                                        'reps': (kb_warmup_reps_list[idx]),
                                                        }

        # BARBELL SELECTION
        barbell_warmup = {}

        barbell_movements_from_todays_wod = get_which_movements_are_barbell_movements(todays_wod)
        barbell_warmup_movements_list = get_barbell_warmup_movements(todays_wod)
        barbell_warmup_text_list = get_text_for_display(barbell_warmup_movements_list, barbell_warmups_dict)
        barbell_warmup_img_list = get_images_for_display(barbell_warmup_movements_list, barbell_warmups_dict)
        barbell_warmup_url_list = get_url_for_display(barbell_warmup_movements_list, barbell_warmups_dict)
        barbell_warmup_reps_list = get_reps(barbell_warmup_movements_list, tough_exercises, barbell_warmups_dict)
        for idx, item in enumerate(barbell_warmup_movements_list):
            barbell_warmup[barbell_warmup_movements_list[idx]] = {'img': (barbell_warmup_img_list[idx]),
                                                                  'url': (barbell_warmup_url_list[idx]),
                                                                  'text': (barbell_warmup_text_list[idx]),
                                                                  'reps': (barbell_warmup_reps_list[idx])
                                                                  }
        est_time_for_display = get_est_times_for_display(metcon_warmup, drom_warmup[0], gymnastics_final_dict,
                                                         kb_warmup, barbell_warmup)[0]
        est_time_for_display_plus5 = get_est_times_for_display(metcon_warmup, drom_warmup[0], gymnastics_final_dict,
                                                               kb_warmup, barbell_warmup)[1]

        return render_template('index.html', drom_warmup=drom_warmup, metcon_warmup=metcon_warmup,
                               exercise_keys=exercise_keys,
                               barbell_warmup=barbell_warmup,
                               barbell_movements_from_todays_wod=
                               barbell_movements_from_todays_wod,
                               kb_movements_from_todays_wod=kb_movements_from_todays_wod,
                               kb_warmup=kb_warmup, tough_gymnastics_movements_from_todays_wod=
                               tough_gymnastics_movements_from_todays_wod,
                               easy_exercises=easy_exercises, tough_exercises=tough_exercises,
                               gymnastics_final_dict=gymnastics_final_dict, drom_final_dict=drom_final_dict,
                               todays_wod=todays_wod, est_time_for_display=est_time_for_display,
                               est_time_for_display_plus5=est_time_for_display_plus5,
                               error_message=error_message, warmup_duration_selection=warmup_duration_selection,
                               gearcheck1 = gearcheck1, gearcheck2 = gearcheck2,
                               print_for_debug=print_for_debug
                               )

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html', exercise_keys=exercise_keys,
                               warmup_duration_selection=warmup_duration_selection)
