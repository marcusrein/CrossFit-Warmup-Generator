## Meditate on this
## Fill out more dummy functions to make them actually work
## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)

#TODO: make dropdowns for input

from getters import *
from filters import *
from checks import *

from exercises_dataset import *
from fuzzywuzzy import fuzz
from flask import Flask, render_template, request

app = Flask(__name__)

########################################   @ FUNCTIONS  @   #########################################################


def get_droms_compiled(intensity, todays_wod, todays_wod_toggles):
    """This is a function that compiles DROMS for viewing."""
    todays_wod = remove_none_from_todays_wod(todays_wod)

    ##CHECKS##
    has_kb_exercise = check_kb_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    has_tough_gymnastics = check_tough_gymnastics(todays_wod)

    ##GETTERS##
    mov_cat = get_cat_from_todays_wod(todays_wod)
    todays_possible_droms = get_possible_droms_from_mov_cat(mov_cat)
    drom_tally_organized_dict = get_organized_drom_tally_dict(todays_possible_droms)
    drom_tally_organized_times_list = get_times_of_organized_drom_tally_list(drom_tally_organized_dict)
    drom_tally_organized_times_sum = get_sum_times_of_list(drom_tally_organized_times_list)
    all_warmup_times_pre_toggle = get_all_warmup_times(todays_wod, intensity)
    drom_prescribed_time = all_warmup_times_pre_toggle['drom_time']
    all_warmup_times_plus_toggles = check_toggles_add_time(todays_wod, todays_wod_toggles, all_warmup_times_pre_toggle)
    selected_droms = pop_and_select(drom_tally_organized_dict, drom_tally_organized_times_list,
                                    drom_tally_organized_times_sum, drom_prescribed_time)

    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod, 'intensity': intensity,
            'has kb exercise': has_kb_exercise,
            'has barbell exercise': has_barbell_exercise,
            'has_tough_gymnastics': has_tough_gymnastics, 'todays_wod_toggles': todays_wod_toggles,
            'ALL WARMUP TIMES PLUS TOGGLES ': all_warmup_times_plus_toggles,
            'DROM CALCULATIONS: ''mov_cat': mov_cat,
            'todays possible droms': todays_possible_droms, 'DROM TALLY ORGANIZED DICT': drom_tally_organized_dict,
            'drom tally organized times list': drom_tally_organized_times_list,
            'drom tally organized times sum': drom_tally_organized_times_sum,
            'drom prescribed time': drom_prescribed_time, 'SELECTED DROMS: ': selected_droms
            }

########################################   @ APP ROUTES  @   #########################################################

@app.route('/', methods=['GET', 'POST'])
def first_page():
    if request.method == 'POST':
        intensity = request.form['intensity_form']
        exercise1 = check_exercise_fuzz_80(request.form['exercise1_form'])
        exercise2 = check_exercise_fuzz_80(request.form['exercise2_form'])
        exercise3 = check_exercise_fuzz_80(request.form['exercise3_form'])
        exercise4 = check_exercise_fuzz_80(request.form['exercise4_form'])
        exercise5 = check_exercise_fuzz_80(request.form['exercise5_form'])

        exercise1_toggle = request.form['exercise1_toggle']
        exercise2_toggle = request.form['exercise2_toggle']
        exercise3_toggle = request.form['exercise3_toggle']
        exercise4_toggle = request.form['exercise4_toggle']
        exercise5_toggle = request.form['exercise5_toggle']

        todays_wod = [exercise1, exercise2, exercise3, exercise4, exercise5]
        todays_wod_toggles = [exercise1_toggle, exercise2_toggle, exercise3_toggle, exercise4_toggle, exercise5_toggle]
        warmups_compiled = get_droms_compiled(intensity, todays_wod, todays_wod_toggles)

        return render_template('index.html', warmups_compiled=warmups_compiled)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


