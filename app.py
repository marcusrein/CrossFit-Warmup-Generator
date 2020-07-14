import sys
from getters import *
from flask import Flask, render_template, request
from barbell_warmups import *
from kb_warmups import *
from media import *
import itertools
app = Flask(__name__)

# TODO: * cant get height right for mobile dropdown
# TODO: * spacing of pill in sidebar during phone orientation
# TODO: * display warms up these exercises as pills or
# TODO: * get all the dropdown HREF things to work correctly in sidebar small screen, then center the items
# TODO: * dont let 0.1 on the logo drop down so early
# TODO: * Get screen orientation to lock in portrait mode
# TODO: * card does not display fully on dropdowns

# TODO: add draggable inputs
# TODO: get "warms up these exercises" to appear in phone sidebar
# TODO: Create banded section.
# TODO: Pullups warmups not appearing in output
# TODO: 1. Create DB category throughout code, 2. fix bug in index.html that doubles-up input (it lookslike
#  I can put in airsquat 2x) 3. create 'equipment' thing. 4. have users log in

@app.route('/', methods=['GET', 'POST'])
def first_page():
    from exercises import exercises_dict
    from droms import droms_dict

    alphabetical_exercises_dict = OrderedDict(sorted(exercises_dict.items(), key=lambda x: x[0]))
    exercise_keys = alphabetical_exercises_dict.keys()

    metcon_time = 'metcon_time'
    drom_time = 'drom_time'

    background_image = media_dict['barbell']['img']

    print(background_image)

    if request.method == 'POST':
        # INPUT
        easy_exercises = request.form.getlist('easy_exercises_form')
        easy_exercises = [easy_exercise.lower() for easy_exercise in easy_exercises]
        tough_exercises = request.form.getlist('tough_exercises_form')
        tough_exercises = [tough_exercise.lower() for tough_exercise in tough_exercises]

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

        # DROM SELECTION AND IMAGE SELECTION
        droms_compiled = get_movements_compiled(
            todays_wod, tough_exercises, droms_dict, drom_time)
        selected_droms = droms_compiled.get('SELECTED MOVEMENTS: ')
        # print('selectedDROMS: ', selected_droms)
        addendum_droms = get_selected_movements_addendum_droms(todays_wod, selected_droms, selected_metcon)
        # print('addendumDROMS: ', addendum_droms)
        if addendum_droms:
            try:
                for i in range(len(addendum_droms)):
                    selected_droms.pop()
                for item in addendum_droms:
                    selected_droms.insert(0, item)
            except IndexError:
                selected_droms = addendum_droms
        # print('selected_DROMS after addendums added: ',selected_droms)
        selected_droms_after_ordered_list = get_ordered_drom_list(selected_droms)
        # print('selected drom after addendums and orderings:', selected_droms_after_ordered_list)
        selected_droms_after_addendums_and_odd_conditionals = get_insert_remove_odd_conditionals_droms(
            selected_droms_after_ordered_list, selected_metcon)
        # print('selectedDROMS after addendums, orderings, and odd condiontlas',
        # selected_droms_after_addendums_and_odd_conditionals)
        selected_droms = selected_droms_after_addendums_and_odd_conditionals
        # print(selected_droms)


        ###### KEY CODING TO COMBINE MULTIPLE LISTS INTO A SINGLE DICTIONARY  #####
        drom_final_dict = {}

        drom_img_list = get_images_for_display(selected_droms, droms_dict)
        drom_reps = get_reps(selected_droms, tough_exercises, droms_dict)
        # USED FOR ITERATING COLLAPSABLE DROPDOWNS IN INDEX.HTML
        # list_of_numbers_for_collapsable_dropdowns = get_length_of_final_drom_dict_for_index_dropdowns(drom_reps)
        # print(list_of_numbers_for_collapsable_dropdowns)

        rand_words_for_accordion00 = get_random_word_for_accordions00(drom_reps)
        rand_words_for_accordion0 = get_random_word_for_accordions0(drom_reps)
        rand_words_for_accordion1 = get_random_word_for_accordions1(drom_reps)
        rand_words_for_accordion2 = get_random_word_for_accordions2(drom_reps)
        for idx, item in enumerate(drom_img_list):
            drom_final_dict[selected_droms[idx]] = {'img': (drom_img_list[idx]), 'reps': (drom_reps[idx]),
                                                    # 'dropdowns_rand00': (rand_words_for_accordion00[idx]),
                                                    # 'dropdowns_rand0': (rand_words_for_accordion0[idx]),
                                                    # 'dropdowns_rand1': (rand_words_for_accordion1[idx]),
                                                    # 'dropdowns_rand2': (rand_words_for_accordion2[idx]),
                                                    # 'targets':?[idx])
                                                    }
        why_drom = get_why_drom_selected_dict(drom_final_dict, todays_wod)
        this = add_why_drom_selected_to_drom_final_dict(drom_final_dict, why_drom)
        print(this)






        # GYMNASTICS SELECTION
        tough_gymnastics_movements_from_todays_wod = which_movements_are_tough_gymnastics_movements(todays_wod)
        tough_gymnastics_warmups = get_gymnastics_warmup(todays_wod)

        gymnastics_final_dict = {}

        for k, v in gymnastics_warmups.items():
            for tough_gymnastics_movement in tough_gymnastics_warmups:
                if tough_gymnastics_movement == k:
                    gymnastics_final_dict[k] = v

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

        return render_template('index.html', droms_compiled=droms_compiled, metcon_warmup=metcon_warmup,
                               exercise_keys=exercise_keys, selected_droms=selected_droms,
                               barbell_warmup=barbell_warmup,
                               barbell_movements_from_todays_wod=
                               barbell_movements_from_todays_wod,
                               kb_movements_from_todays_wod=kb_movements_from_todays_wod,
                               kb_warmup=kb_warmup, tough_gymnastics_movements_from_todays_wod=
                               tough_gymnastics_movements_from_todays_wod,
                               easy_exercises=easy_exercises, tough_exercises=tough_exercises,
                               gymnastics_final_dict=gymnastics_final_dict, drom_final_dict=drom_final_dict,
                               todays_wod=todays_wod, error_message=error_message, background_image=background_image,
                               this=this)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html', exercise_keys=exercise_keys, background_image=background_image)


if __name__ == '__main__':
    app.run(debug=True)
