from getters import *
from checks import *
from flask import Flask, render_template, request

app = Flask(__name__)

# TODO: 1. Change toggle routing, 2. Get gymnastics warmup to populate properly. 3. Program for various BB Warmups

@app.route('/', methods=['GET', 'POST'])
def first_page():
    from exercises import exercises
    from droms import droms

    exercise_keys = exercises.keys()

    metcon_time = 'metcon_time'
    drom_time = 'drom_time'

    # length_of_x = len(x)
    if request.method == 'POST':
        # intensity = request.form['intensity_form']

        # exercise1 = check_exercise_fuzz_80(request.form['exercise1_form'])
        # exercise2 = check_exercise_fuzz_80(request.form['exercise2_form'])
        # exercise3 = check_exercise_fuzz_80(request.form['exercise3_form'])
        # exercise4 = check_exercise_fuzz_80(request.form['exercise4_form'])
        # exercise5 = check_exercise_fuzz_80(request.form['exercise5_form'])

        easy_exercises = request.form.getlist('easy_exercises_form')
        tough_exercises = request.form.getlist('tough_exercises_form')

        # exercise1_toggle = request.form['exercise1_toggle']
        # exercise2_toggle = request.form['exercise2_toggle']
        # exercise3_toggle = request.form['exercise3_toggle']
        # exercise4_toggle = request.form['exercise4_toggle']
        # exercise5_toggle = request.form['exercise5_toggle']

        # todays_wod = [exercise1, exercise2, exercise3, exercise4, exercise5]

        todays_wod = easy_exercises + tough_exercises

        todays_wod = remove_none_from_todays_wod(todays_wod)

        # todays_wod_toggles = [exercise1_toggle, exercise2_toggle,
        #                       exercise3_toggle, exercise4_toggle, exercise5_toggle]

        """ GOTTA MAKE CODE THAT SAYS 'IF TOUGH EXERCISE, automaticcaly make it toggle YES"""

        """ DUMMY CODE!! """
        todays_wod_toggles = ['No', 'No', 'No', 'No', 'No', 'Yes']
        """ DUMMY CODE!! """

        metcons_compiled = get_movements_compiled(
            todays_wod, tough_exercises, metcons, metcon_time)
        selected_metcon = metcons_compiled.get('SELECTED MOVEMENTS: ')
        cleaned_metcon_reps = ''.join(str(x) for x in selected_metcon)
        metcon_reps = get_metcon_reps(cleaned_metcon_reps)

        droms_compiled = get_movements_compiled(
            todays_wod, tough_exercises, droms, drom_time)
        selected_droms = droms_compiled.get('SELECTED MOVEMENTS: ')

        drom_img_list = get_images_for_display(selected_droms, droms)
        drom_images_dict = dict(zip(selected_droms, drom_img_list))

        barbell_warmup = []
        barbell_movements_from_todays_wod = which_movements_are_barbell_movements(todays_wod)
        if barbell_movements_from_todays_wod:
            barbell_warmup = barbell_loader(todays_wod)

        kb_warmup = []
        kb_movements_from_todays_wod = which_movements_are_kb_movements(todays_wod)
        if kb_movements_from_todays_wod:
            kb_warmup = kettlebell_loader(todays_wod)

        tough_gymnastics_wu_and_reps_dict = {}

        tough_gymnastics_warmups = []
        tough_gymnastics_movements_from_todays_wod = which_movements_are_tough_gymnastics_movements(todays_wod)
        if tough_gymnastics_movements_from_todays_wod:
            tough_gymnastics_warmups = gymnastics_loader(todays_wod)
            tough_gymnastics_reps = gymnastics_rep_finder(tough_gymnastics_warmups)
            tough_gymnastics_wu_and_reps_dict = dict(zip(tough_gymnastics_warmups, tough_gymnastics_reps))

        tough_gymnastics_img_list = get_images_for_display(tough_gymnastics_warmups, loading)
        tough_gymnastics_img_dict = dict(zip(tough_gymnastics_warmups, tough_gymnastics_img_list))

        return render_template('index.html', droms_compiled=droms_compiled, selected_metcon=selected_metcon,
                               metcon_reps=metcon_reps, exercise_keys=exercise_keys, selected_droms=selected_droms,
                               drom_images_dict=drom_images_dict, barbell_warmup=barbell_warmup,
                               barbell_movements_from_todays_wod=
                               barbell_movements_from_todays_wod,
                               kb_movements_from_todays_wod=kb_movements_from_todays_wod,
                               kb_warmup=kb_warmup, tough_gymnastics_movements_from_todays_wod=
                               tough_gymnastics_movements_from_todays_wod,
                               tough_gymnastics_wu_and_reps_dict=tough_gymnastics_wu_and_reps_dict,
                               tough_gymnastics_img_dict=tough_gymnastics_img_dict, easy_exercises=easy_exercises,
                               tough_exercises=tough_exercises)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html', exercise_keys=exercise_keys)


if __name__ == '__main__':
    app.run(debug=True)
