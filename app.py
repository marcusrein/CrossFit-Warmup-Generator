import barbell_warmups
from getters import *
from flask import Flask, render_template, request
from barbell_warmups import *
from kb_warmups import *

app = Flask(__name__)

# TODO: fix if no input, site crashes
# TODO: href not working
# TODO: 1. Create DB category throughout code, 2. fix bug in index.html that doubles-up input (it lookslike
#  I can put in airsquat 2x) 3. create 'equipment' thing. 4. have users log in 5. figure out barbell loading

@app.route('/', methods=['GET', 'POST'])
def first_page():
    from exercises import exercises
    from droms import droms

    exercise_keys = exercises.keys()

    metcon_time = 'metcon_time'
    drom_time = 'drom_time'

    if request.method == 'POST':
        # INPUT
        easy_exercises = request.form.getlist('easy_exercises_form')
        easy_exercises = [easy_exercise.lower() for easy_exercise in easy_exercises]
        tough_exercises = request.form.getlist('tough_exercises_form')
        tough_exercises = [tough_exercise.lower() for tough_exercise in tough_exercises]

        # TODAYSWOD
        todays_wod = easy_exercises + tough_exercises

        # METCON SELECTION
        # breakpoint()
        metcons_compiled = get_movements_compiled(
            todays_wod, tough_exercises, metcons, metcon_time)
        selected_metcon = metcons_compiled.get('SELECTED MOVEMENTS: ')
        cleaned_metcon_reps = ''.join(str(x) for x in selected_metcon)
        metcon_reps = get_metcon_reps(cleaned_metcon_reps)

        # DROM SELECTION AND IMAGE SELECTION

        droms_compiled = get_movements_compiled(
            todays_wod, tough_exercises, droms, drom_time)
        selected_droms = droms_compiled.get('SELECTED MOVEMENTS: ')
        # print('PREPROCCESING SELECTED DROMS: ', selected_droms)
        addendum_droms = get_selected_movements_addendum_droms(todays_wod, selected_droms)
        protected_droms = []
        # print(todays_wod)
        # print('selectedDROMS: ', selected_droms)
        # print('addendumDROMS: ', addendum_droms)
        if addendum_droms:
            # for addendum_drom in addendum_droms:
            #     for selected_drom in selected_droms:
            #         if addendum_drom == selected_drom:
            #             protected_droms.append(addendum_drom)
            # print('protected: ' ,protected_droms)

            try:
                for i in range(len(addendum_droms)):
                    selected_droms.pop()
                for item in addendum_droms:
                    selected_droms.insert(0, item)
            except IndexError:
                selected_droms = addendum_droms

            ###### KEY CODING TO COMBINE MULTIPLE LISTS INTO A SINGLE DICTIONARY  #####
        drom_img_list = get_images_for_display(selected_droms, droms)
        drom_reps = get_reps(selected_droms, tough_exercises, droms)
        drom_final_dict = {}

        for idx, item in enumerate(drom_img_list):
            drom_final_dict[selected_droms[idx]] = {'img': (drom_img_list[idx]), 'reps': (drom_reps[idx])}

        # BARBELL SELECTION
        barbell_warmup = {}

        barbell_movements_from_todays_wod = which_movements_are_barbell_movements(todays_wod)
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

        # KB SELECTION
        kb_warmup = {}

        kb_movements_from_todays_wod = which_movements_are_kb_movements(todays_wod)
        kb_warmup_movements_list = get_kettlebell_warmup(todays_wod)
        kb_warmup_img_list = get_images_for_display(kb_warmup_movements_list, kb_warmups_dict)
        kb_warmup_url_list = get_url_for_display(kb_warmup_movements_list, kb_warmups_dict)
        kb_warmup_reps_list = get_reps(kb_warmup_movements_list, tough_exercises, kb_warmups_dict)
        for idx, item in enumerate(kb_warmup_movements_list):
            kb_warmup[kb_warmup_movements_list[idx]] = {'img': (kb_warmup_img_list[idx]),
                                                        'url': (kb_warmup_url_list[idx]),
                                                        'reps': (kb_warmup_reps_list[idx]),
                                                        }

        # GYMNASTICS SELECTION
        tough_gymnastics_movements_from_todays_wod = which_movements_are_tough_gymnastics_movements(todays_wod)
        tough_gymnastics_warmups = get_gymnastics_warmup(todays_wod)

        new_gymnastics_temp_dict = {}

        for k, v in gymnastics_warmups.items():
            for tough_gymnastics_movement in tough_gymnastics_warmups:
                if tough_gymnastics_movement == k:
                    new_gymnastics_temp_dict[k] = v
        # breakpoint()
        return render_template('index.html', droms_compiled=droms_compiled, selected_metcon=selected_metcon,
                               metcon_reps=metcon_reps, exercise_keys=exercise_keys, selected_droms=selected_droms,
                               barbell_warmup=barbell_warmup,
                               barbell_movements_from_todays_wod=
                               barbell_movements_from_todays_wod,
                               kb_movements_from_todays_wod=kb_movements_from_todays_wod,
                               kb_warmup=kb_warmup, tough_gymnastics_movements_from_todays_wod=
                               tough_gymnastics_movements_from_todays_wod,
                               easy_exercises=easy_exercises, tough_exercises=tough_exercises,
                               new_gymnastics_temp_dict=new_gymnastics_temp_dict, drom_final_dict=drom_final_dict,
                               todays_wod=todays_wod)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html', exercise_keys=exercise_keys)


if __name__ == '__main__':
    app.run(debug=True)
