from getters import *
from checks import *
from flask import Flask, render_template, request

app = Flask(__name__)

# TODO: 1. Make code more accurate in choosing DROMS (reduce number of things that
#  could be applicable in categories? Increase minutes? Require dependencies [if air squats in workout you must do
#  airsquats in warmup] YEP thats it! Easier is better!. 2. Program for various BB Warmups

@app.route('/', methods=['GET', 'POST'])
def first_page():
    from exercises import exercises
    from droms import droms

    exercise_keys = exercises.keys()

    metcon_time = 'metcon_time'
    drom_time = 'drom_time'

    if request.method == 'POST':
        #INPUT
        easy_exercises = request.form.getlist('easy_exercises_form')
        easy_exercises = [easy_exercise.lower() for easy_exercise in easy_exercises]
        tough_exercises = request.form.getlist('tough_exercises_form')
        tough_exercises = [tough_exercise.lower() for tough_exercise in tough_exercises]

        #TODAYSWOD
        todays_wod = easy_exercises + tough_exercises

        #METCON SELECTION
        metcons_compiled = get_movements_compiled(
            todays_wod, tough_exercises, metcons, metcon_time)
        selected_metcon = metcons_compiled.get('SELECTED MOVEMENTS: ')
        cleaned_metcon_reps = ''.join(str(x) for x in selected_metcon)
        metcon_reps = get_metcon_reps(cleaned_metcon_reps)

        #DROM SELECTION AND IMAGE SELECTION
        droms_compiled = get_movements_compiled(
            todays_wod, tough_exercises, droms, drom_time)
        selected_droms = droms_compiled.get('SELECTED MOVEMENTS: ')
        x = get_selected_movements_addendum_droms(todays_wod, selected_droms)
        if x:
            selected_droms.pop()
            selected_droms.append(x)


        drom_img_list = get_images_for_display(selected_droms, droms)
        drom_images_dict = dict(zip(selected_droms, drom_img_list))

        #BARBELL SELECTION
        barbell_warmup = []
        barbell_movements_from_todays_wod = which_movements_are_barbell_movements(todays_wod)
        if barbell_movements_from_todays_wod:
            barbell_warmup = barbell_loader(todays_wod)

        #KB SELECTION
        kb_warmup = []
        kb_movements_from_todays_wod = which_movements_are_kb_movements(todays_wod)
        if kb_movements_from_todays_wod:
            kb_warmup = kettlebell_loader(todays_wod)

        #GYMNASTICS SELECTION
        tough_gymnastics_movements_from_todays_wod = which_movements_are_tough_gymnastics_movements(todays_wod)
        tough_gymnastics_warmups = gymnastics_loader(todays_wod)

        new_gymnastics_temp_dict = {}

        for k,v in loading.items():
            for tough_gymnastics_movement in tough_gymnastics_warmups:
                if tough_gymnastics_movement == k:
                    new_gymnastics_temp_dict[k] = v

        return render_template('index.html', droms_compiled=droms_compiled, selected_metcon=selected_metcon,
                               metcon_reps=metcon_reps, exercise_keys=exercise_keys, selected_droms=selected_droms,
                               drom_images_dict=drom_images_dict, barbell_warmup=barbell_warmup,
                               barbell_movements_from_todays_wod=
                               barbell_movements_from_todays_wod,
                               kb_movements_from_todays_wod=kb_movements_from_todays_wod,
                               kb_warmup=kb_warmup, tough_gymnastics_movements_from_todays_wod=
                               tough_gymnastics_movements_from_todays_wod,
                               easy_exercises=easy_exercises, tough_exercises=tough_exercises,
                               new_gymnastics_temp_dict=new_gymnastics_temp_dict)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html', exercise_keys=exercise_keys)


if __name__ == '__main__':
    app.run(debug=True)
