## Meditate on this
## Fill out more dummy functions to make them actually work
## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)

import warmups_dataset
import exercises_dataset
from fuzzywuzzy import fuzz
from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, validators

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

app = Flask(__name__)


##THE THING IN QUOTES IS THE KEY
## ACTION = IN THE HTML FILE SENDS THE DATA TO WHERE YOU"VE PUT THE ACTION!!! FUCCCKKKK


########################################   @ FUNCTIONS  @   #########################################################


def check_exercise_fuzz_80(exercise1_prefuzz):
    for j in list(exercises.keys()):
        if (fuzz.ratio(exercise1_prefuzz, j)) > 80:
            return j


def remove_none_from_todays_wod(todays_wod):
    """Remove "none" from todays_wod to clean it up"""
    cleaned_array = []
    for wod in todays_wod:
        if wod != None:
            cleaned_array.append(wod)
    return cleaned_array


def get_droms_compiled(intensity, todays_wod):
    """This is a function that compiles DROMS for viewing."""
    # if intensity == 'low':
    ### if time_prompt is too short and todays WOD has loaded exercise, return a warning (maybe later ask for more time?)
    ### if time prompt is ok
    ### what jj likes to do is return a fake object at first to practice. use the fake data in other functions to get a flow! know where you want to go!
    todays_wod = remove_none_from_todays_wod(todays_wod)
    has_kb_exercise = check_kb_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    has_tough_gymnastics = check_tough_gymnastics(todays_wod)
    mov_cat = get_cat_from_todays_wod(todays_wod)
    todays_possible_droms = get_possible_droms_from_mov_cat(mov_cat)
    drom_tally_organized = get_organized_drom_tally_dict(todays_possible_droms)
    drom_tally_organized_times = get_times_of_organized_drom_tally_list(drom_tally_organized)
    drom_tally_organized_times_sum = get_sum_times_of_list(drom_tally_organized_times)
    all_warmup_times = get_all_warmup_times(todays_wod,intensity)
    drom_prescribed_time = all_warmup_times['drom_time']
    pop_list(drom_tally_organized, drom_tally_organized_times, drom_prescribed_time)

    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod,'intensity': intensity,
            'has kb exercise': has_kb_exercise,
            'has barbell exercise': has_barbell_exercise,
            'has_tough_gymnastics': has_tough_gymnastics, 'DROM CALCULATIONS: ''mov_cat': mov_cat,
            'todays possible droms': todays_possible_droms, 'drom tally organized': drom_tally_organized,
            'drom tally organized times': drom_tally_organized_times,
            'drom tally organized times sum': drom_tally_organized_times_sum,
            'drom prescribed time': drom_prescribed_time,
            }
    ## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)


# def check_loaded_exercise(todays_wod):
#     for wod in todays_wod:
#         if not exercises[wod]['loaded']:
#             return False
#         else:
#             return True


#                                    TODO add in metcon option in future.
# def check_focus_empty(focus):
#     if not focus:
#         return True
#     else:
#         return False


# def check_focus_gymnastics(focus):
#     for k, v in exercises.items():
#         if focus == k:
#             if v['category'] == 'gymnastics upper' or v['category'] == 'gymnastics lower':
#                 return True
#             else:
#                 return False

# def check_focus_barbell(focus):
#     for k, v in exercises.items():
#         if focus == k:
#             if v['loaded'] == 'barbell':
#                 return True
#             else:
#                 return False


# def check_focus_kb(focus):
#     for k, v in exercises.items():
#         if focus == k:
#             if v['loaded'] == 'kb':
#                 return True
#             else:
#                 return False
#             # elif v['loaded'] == 'kb':
#             #     return 'kb'


## Note 5/4 JORDAAAYYY: I noticed that if I just put one exercise in the exercise1 HTML input, my code checks it 5 times because
## todays_wod has "none" defaulted when theres nothing inputted. i dont need this to run! It's affecting check_kb_exercise,
## check_barbell_exercise, and likely everything else.

def check_kb_exercise(todays_wod):
    # print(todays_wod)
    for wod in todays_wod:
        # print(wod)
        if exercises[wod]['loaded'] == 'kb':
            return True


def check_barbell_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == 'barbell':
            return True


def check_tough_gymnastics(todays_wod):
    words = ['pistol', 'pistols', 'handstand', 'pull up', 'pull ups', 'kipping', 'ring', 'muscle up']
    check = any(item in words for item in todays_wod)
    if check:
        return True


def get_cat_from_todays_wod(todays_wod):
    todays_cat = []
    for w in todays_wod:
        for k, v in exercises.items():
            if w == k:
                todays_cat.append(v['category'])
    return todays_cat


def get_possible_droms_from_mov_cat(mov_cat):
    possible_warmups = []
    for cat in mov_cat:
        for k, v in warmups.items():
            if cat in v['categories']:
                possible_warmups.append(k)
    return possible_warmups


def get_organized_drom_tally_dict(possible_warmups):
    tally_of_warmups = {}
    for w in possible_warmups:
        if w in tally_of_warmups:
            tally_of_warmups[w] += 1
        else:
            tally_of_warmups[w] = 1
    ordered_tally = {k: v for k, v in sorted(tally_of_warmups.items(), key=lambda item: item[1], reverse=True)}
    return ordered_tally


def get_times_of_organized_drom_tally_list(ordered_tally):
    """Puts times of organized warmup tally into a separate list"""
    tally_of_warmups_times = []
    for k, v in ordered_tally.items():
        for k2, v2 in warmups.items():
            if k == k2:
                tally_of_warmups_times.append(v2['time'])
    return tally_of_warmups_times

def pop_list(dict, dict_organized_times, prescribed_time):
    """
    dict = dict of ordered tally
    dict_organized_times = dict of the ordered tallies times
    time_alloted = time alloted by get_all_warmup_times
    return: Popped list
    """
    while sum(dict_organized_times) > prescribed_time:
        dict.pop()

    else:
        print('nope!')

def get_sum_times_of_list(x):  ###ENDED CODING HERE. STARTING TO WORK ON FIGURING OUT HOW TO GET IDEAL TIME FOR WARMUP... ALSO TOTAL TIME... WRITE THIS OUT ON PAPER BEFORE GOING FARTHER
    """Sums any list of numbers"""
    sum_times = sum(x)
    return sum_times


def get_all_warmup_times(todays_wod, intensity):
    metcon_time = 0
    drom_time = 0
    gymnastics_time = 0
    barbell_time = 0
    kb_time = 0
    focused_gymnastics_time = 0
    focused_barbell_time = 0
    focused_kb_time = 0

    # print(check_focus_barbell(focus))
    # print(check_barbell_exercise(todays_wod))
    # print(check_tough_gymnastics(todays_wod))

    ## LOW GYMNASTICS ##
    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 5
        barbell_time += 5
        kb_time += 5
        focused_gymnastics_time += 10
        print('TTT')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 5
        barbell_time += 5
        kb_time += 5
        focused_gymnastics_time += 10
        print('TTF')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 5
        barbell_time += 5
        focused_gymnastics_time += 10
        print('TFT')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 5
        barbell_time += 5
        print('TFF')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 5
        kb_time += 5
        focused_gymnastics_time += 10
        print('FTT')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 3
        drom_time += 5
        kb_time += 5
        print('FTF')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 3
        drom_time += 7
        focused_gymnastics_time += 10
        print('FFT')

    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 5
        drom_time += 5
        print('FFF')

    # NOT NEEDED IF LOADED, WE MOVE ONTO BB OR KB TESTING
    # if intensity == 'low' \
    #         and check_focus_category(focus) == 'gymnastics' \
    #         and check_loaded_exercise(todays_wod) == True \
    #         and check_tough_gymnastics(todays_wod) == True:
    #     metcon_time += 2
    #     drom_time += 5
    #     loaded_warmup_time += 5
    #     focused_gymnastics_time += 10
    #     print('aoiwjef')

    all_warmup_time = (
            metcon_time + drom_time + gymnastics_time + barbell_time + kb_time + focused_gymnastics_time + focused_barbell_time + focused_kb_time)

    calculated_times = {'all_warmup_time': all_warmup_time, 'metcon_time': metcon_time, 'drom_time': drom_time}
    print(calculated_times)

    return calculated_times


# DUMMY FUNCTIONS todo: Fill out these dummy functions!

#     metcon_time = 0
#     drom_time = 0
#     gymnastics_time = 0
#     barbell_time = 0
#     kb_time = 0
#     focused_gymnastics_time = 0
#     focused_barbell_time = 0
#     focused_kb_time = 0

# def prioritize_pop_metcon(todays_wod):
#     """Prioritizes and pops metcons as compared to total time alloted"""
#     return tallied list in order of importance
#
def prioritize_pop_droms():
    """Prioritizes and pops DROMS as compared to total time alloted"""


# def prioritize_pop_gymnastics_wu(todays_wod):
#     """Prioritizes and pops tough_gymnastics as compared to total time alloted"""
#     return tallied list in order of importance

# def prioritize_pop_kb_wu(todays_wod):
#     """Prioritizes and pops kb_warmups as compared to total time alloted"""
#     return tallied list in order of importance

# def prioritize_pop_barbell_wu(todays_wod):
#     """Prioritizes and pops barbell_wu as compared to total time alloted"""
#     return tallied list in order of importance

# def prioritize_pop_focused_gymnastics_wu(todays_wod):
#     """Prioritizes and pops tough_gymnastics as compared to total time alloted"""
#     return tallied list in order of importance

# def prioritize_pop_focused_kb_wu(todays_wod):
#     """Prioritizes and pops kb_warmups as compared to total time alloted"""
#     return tallied list in order of importance

# def prioritize_pop_focused_barbell_wu(todays_wod):
#     """Prioritizes and pops barbell_wu as compared to total time alloted"""
#     return tallied list in order of importance


# FUNCTIONS ARE LITTLE MACHINES THAT TAKE STUFF AND MAKE IT INTO OTHER STUFF
# ### FAKE DATA OUTPUT WARMUPLITTLEDICT
# def get_warmup_info(wod, intensity):
#     warmup_little_dict = {
#         'walking lunges': {
#             'categories': ['squats', 'cleans', 'deadlifts', 'gymnastics lower', 'kettlebells'],
#             'time': 1,
#             'reps': ['10 reps', '20 reps', '30 reps'],
#             'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
#         },
#         'air squats': {
#             'categories': ['squats', 'squats', 'squats', 'cleans', 'deadlifts', 'gymnastics lower'],
#             'time': 1,
#             'reps': ['10 reps', '20 reps', '30 reps'],
#             'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
#         },
#         'spidermans': {
#             'categories': ['squats', 'cleans', 'deadlifts', 'snatches', 'gymnastics lower'],
#             'time': 2,
#             'reps': ['2 min'],
#             'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
#         }}
#
#     return warmup_little_dict


# def convert_intensity_to_time(intensity):
#

########################################   @ APP ROUTES  @   #########################################################
# TODO: add fuzzy functionality

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
        warmups_compiled = get_droms_compiled(intensity, todays_wod)

        return render_template('index.html', warmups_compiled=warmups_compiled)

    else:
        print('else block called$$$$$$$$$$$$$$$$$$$$$$')
        return render_template('index.html')


@app.route('/get_exercises', methods=['GET', 'POST'])
def second_page():
    global exercise1
    global exercise2
    if request.method == 'POST':
        exercise1 = request.form['exercise1_form']
        exercise2 = request.form['exercise2_form']

        return render_template('tester.html', exercise1=exercise1, exercise2=exercise2)

    else:
        return render_template('tester2.html')


#         time_prompt = request.form['time_prompt']
#         exercise1 = request.args.get('exercise_1')
#         exercise2 = request.args.get('exercise_2')
#         return render_template('tester.html', exercise1=exercise1, exercise2=exercise2, time_prompt=time_prompt)
#
#     else:
#         return render_template('say_time.html')

# '''<h4>The first exercise is {} and its interals are {}<h4>
# <h4>The second exercise is {} and its internals are {}<h4>'''.format(exercise1, exercises[exercise1], exercise2, exercises[exercise2])

if __name__ == '__main__':
    app.run(debug=True)

########################################### UNUSED CODE ##############################################


# warmups = []
# for wod in todays_wod:
#     x = get_warmup_info(wod,intensity)
#     warmups.append(x)
# print(intensity)
# print(todays_wod)
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# return [{'warmup_name':'air squats', 'time': '2min'},{'warmup_name':'walking lunges', 'time':'1min'}]
