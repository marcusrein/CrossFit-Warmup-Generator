## Meditate on this
## Fill out more dummy functions to make them actually work
## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)

import warmups_dataset
import exercises_dataset
from fuzzywuzzy import fuzz

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request
app = Flask(__name__)

##THE THING IN QUOTES IS THE KEY
## ACTION = IN THE HTML FILE SENDS THE DATA TO WHERE YOU"VE PUT THE ACTION!!! FUCCCKKKK


########################################   @ FUNCTIONS  @   #########################################################


def get_warmups_compiled(intensity,todays_wod,focus):
    """This is the big one that processes all the data."""
    # if intensity == 'low':
    ### if time_prompt is too short and todays WOD has loaded exercise, return a warning (maybe later ask for more time?)
    ### if time prompt is ok
    ### what jj likes to do is return a fake object at first to practice. use the fake data in other functions to get a flow! know where you want to go!
    has_loaded_exercise = check_loaded_exercise(todays_wod)
    has_kb_exercise = check_kb_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    mov_cat = get_cat_from_todays_wod(todays_wod)
    todays_possible_warmups = get_possible_warmups_from_mov_cat(mov_cat)
    warmup_tally_organized = get_organized_warmup_tally(todays_possible_warmups)
    warmup_tally_organized_times = get_times_of_organized_warmup_tally(warmup_tally_organized)
    warmup_tally_organized_times_sum = get_sum_times_of_list(warmup_tally_organized_times)

    optimal_warmup_time = get_optimal_warmup_time(todays_wod,intensity,focus)

    # optimal_warmup_time = get_optimal_warmup_time(intensity,has_loaded_exercise,has_kb_exercise,has_barbell_exercise)

    return {'todays wod':todays_wod,'mov_cat':mov_cat,'todays possible warmups':todays_possible_warmups,'warmup tally organized':warmup_tally_organized,'warmup tally organized times':warmup_tally_organized_times,'warmup tally organized times sum':warmup_tally_organized_times_sum,'optimal_warmup_time':optimal_warmup_time,'intensity':intensity,'has_loaded_exercise':has_loaded_exercise,'has_kb_exercise':has_kb_exercise,'has_barbell_exercise':has_barbell_exercise,'focus':focus}
    ## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)


def check_loaded_exercise(todays_wod):
    for wod in todays_wod:
        if not exercises[wod]['loaded']:
            return False
        else:
            return True

def check_tough_gymnastics(todays_wod):
    words = ['pistol', 'pistols','handstand','pull up','pull ups','kipping','ring']
    check = any(item in words for item in todays_wod)
    if check:
        print('wowoeijrw')
        return True
    else:
        return False
        print('OOOOOOO')

def check_focus_category(focus):
    for k,v in exercises.items():
        if focus == k:
            if v['category'] == 'gymnastics upper' or v['category'] == 'gymnastics lower':
                return 'gymnastics'
                print('yaaaaapoij')
            elif v['loaded'] == 'barbell':
                return 'barbell'
            elif v['loaded'] == 'kb':
                return 'kb'


def check_kb_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == 'kb':
            return True
        else:
            return False

def check_barbell_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == 'barbell':
            return True
        else:
            return False

def get_cat_from_todays_wod(todays_wod):
    todays_cat = []
    for w in todays_wod:
        for k, v in exercises.items():
            if w == k:
                todays_cat.append(v['category'])
    return todays_cat

def get_possible_warmups_from_mov_cat(mov_cat):
    possible_warmups = []
    for cat in mov_cat:
        for k, v in warmups.items():
            if cat in v['categories']:
                possible_warmups.append(k)
    return possible_warmups

def get_organized_warmup_tally(possible_warmups):
    tally_of_warmups = {}
    for w in possible_warmups:
        if w in tally_of_warmups:
            tally_of_warmups[w] += 1
        else:
            tally_of_warmups[w] = 1
    ordered_tally = {k: v for k, v in sorted(tally_of_warmups.items(), key=lambda item: item[1], reverse=True)}
    return ordered_tally

def get_times_of_organized_warmup_tally(ordered_tally):
    '''Puts times of organized warmup tally into a separate list'''
    tally_of_warmups_times = []
    for k, v in ordered_tally.items():
        for k2, v2 in warmups.items():
            if k == k2:
                tally_of_warmups_times.append(v2['time'])
    return tally_of_warmups_times

def get_sum_times_of_list(x): ###ENDED CODING HERE. STARTING TO WORK ON FIGURING OUT HOW TO GET IDEAL TIME FOR WARMUP... ALSO TOTAL TIME... WRITE THIS OUT ON PAPER BEFORE GOING FARTHER
    '''Sums any list of numbers'''
    sum_times = sum(x)
    return sum_times

def get_optimal_warmup_time(todays_wod,intensity,focus):
    metcon_time = 0
    drom_time = 0
    gymnastics_time = 0
    tough_gymnastics_time = 0
    barbell_time = 0
    kb_time = 0
    focused_gymnastics_time = 0
    focused_barbell_time = 0
    focused_kb_time = 0
    focused_unloaded_time = 0

    ## LOW BODYWEIGHT ##

    if intensity == 'low' \
            and check_loaded_exercise(todays_wod) == False \
            and check_tough_gymnastics(todays_wod) == False:

        metcon_time += 2
        drom_time += 4
        gymnastics_time += 4
        print('aaaaaa')

    if intensity == 'low' \
            and check_loaded_exercise(todays_wod) == False \
            and check_tough_gymnastics(todays_wod) == True:

        metcon_time += 2
        drom_time += 5
        tough_gymnastics_time += 6



    ## LOW BARBELL ##

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_barbell_exercise([focus]) == False \
            and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 2
        drom_time += 4
        barbell_time += 5
        print('C')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_barbell_exercise([focus]) == True \
            and check_tough_gymnastics(todays_wod) == False\
            :
        metcon_time += 2
        drom_time += 5
        focused_barbell_time += 6
        print('D')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_barbell_exercise([focus]) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 6
        focused_barbell_time += 6
        tough_gymnastics_time += 6
        print('e')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_barbell_exercise([focus]) == False \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 4
        barbell_time += 4
        tough_gymnastics_time += 7
        print('f')


    ## LOW KB ##

    elif intensity == 'low' \
            and check_kb_exercise(todays_wod) == True \
            and check_kb_exercise([focus]) == False \
            and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 2
        drom_time += 5
        kb_time += 5
        print('g')

    elif intensity == 'low' \
            and check_kb_exercise(todays_wod) == True \
            and check_kb_exercise([focus]) == True \
            and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 2
        drom_time += 5
        gymnastics_time += 5
        kb_time += 5
        print('h')

    elif intensity == 'low' \
            and check_kb_exercise(todays_wod) == True \
            and check_kb_exercise([focus]) == True \
            and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 2
        drom_time += 5
        focused_kb_time += 8
        print('i')

    elif intensity == 'low' \
            and check_kb_exercise(todays_wod) == True \
            and check_kb_exercise([focus]) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 5
        gymnastics_time += 5
        focused_kb_time += 5
        print('j')


    elif intensity == 'low' \
            and check_kb_exercise(todays_wod) == True \
            and check_kb_exercise([focus]) == False \
            and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 2
        drom_time += 4
        kb_time += 4
        print('k')

    ## MED INTENSITY ##

    ## MED BODYWEIGHT ##

    if intensity == 'medium' and check_loaded_exercise(todays_wod) == False and check_tough_gymnastics(
            todays_wod) == False:
        metcon_time += 3
        drom_time = 5
        print('1')

    elif intensity == 'medium' and check_loaded_exercise(todays_wod) == False and check_tough_gymnastics(
            todays_wod) == True:
        metcon_time += 3
        drom_time = 5
        gymnastics_time += 5
        print('B')

        ## medium BODYWEIGHT BARBELL ##

    elif intensity == 'medium' and check_barbell_exercise(todays_wod) == True and check_barbell_exercise(
            [focus]) == False and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 3
        drom_time += 5
        barbell_time += 5
        print('C')

    elif intensity == 'medium' and check_barbell_exercise(todays_wod) == True and check_barbell_exercise(
            [focus]) == False and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 3
        drom_time += 5
        gymnastics_time += 5
        barbell_time += 5
        print('D')

    elif intensity == 'medium' and check_barbell_exercise(todays_wod) == True and check_barbell_exercise(
            [focus]) == True and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 3
        drom_time += 5
        focused_barbell_time += 10
        print('e')

    elif intensity == 'medium' and check_barbell_exercise(todays_wod) == True and check_barbell_exercise(
            [focus]) == True and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 3
        drom_time += 8
        gymnastics_time += 7
        focused_barbell_time += 10
        print('f')

        ## medium KB ##

    elif intensity == 'medium' and check_kb_exercise(todays_wod) == True and check_kb_exercise(
            [focus]) == False and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 3
        drom_time += 6
        kb_time += 5
        print('g')

    elif intensity == 'medium' and check_kb_exercise(todays_wod) == True and check_kb_exercise(
            [focus]) == False and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 3
        drom_time += 5
        gymnastics_time += 7
        kb_time += 5
        print('h')

    elif intensity == 'medium' and check_kb_exercise(todays_wod) == True and check_kb_exercise(
            [focus]) == True and check_tough_gymnastics(todays_wod) == False:
        metcon_time += 3
        drom_time += 5
        focused_kb_time += 8
        print('i')

    elif intensity == 'medium' and check_kb_exercise(todays_wod) == True and check_kb_exercise(
            [focus]) == True and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 3
        drom_time += 5
        gymnastics_time += 5
        focused_kb_time += 7
        print('j')




    optimal_warmup_time = (metcon_time + drom_time + gymnastics_time + barbell_time + kb_time + focused_gymnastics_time + focused_barbell_time + focused_kb_time + focused_unloaded_time)


    ### DUMMY FUNC
    return optimal_warmup_time
#
# def check_exercise_fuzz_80(exercise1_prefuzz):
#     for j in list(exercises.keys()):
#         if (fuzz.ratio(exercise1_prefuzz, j)) > 80:
#             return True

#FUNCTIONS ARE LITTLE MACHINES THAT TAKE STUFF AND MAKE IT INTO OTHER STUFF
### FAKE DATA OUTPUT WARMUPLITTLEDICT
def get_warmup_info(wod,intensity):

    warmup_little_dict = {
        'walking lunges': {
        'categories': ['squats', 'cleans', 'deadlifts', 'gymnastics lower', 'kettlebells'],
        'time': 1,
        'reps': ['10 reps', '20 reps', '30 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    },
    'air squats': {
        'categories': ['squats', 'squats', 'squats', 'cleans', 'deadlifts', 'gymnastics lower'],
        'time': 1,
        'reps': ['10 reps', '20 reps', '30 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    },
    'spidermans': {
        'categories': ['squats', 'cleans', 'deadlifts', 'snatches', 'gymnastics lower'],
        'time': 2,
        'reps': ['2 min'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    }}

    return warmup_little_dict

# def convert_intensity_to_time(intensity):
#

########################################   @ APP ROUTES  @   #########################################################
# TODO: add fuzzy functionality

@app.route('/', methods=['GET', 'POST'])
def first_page():

    if request.method == 'POST':
        intensity = request.form['intensity_form']
        exercise1= request.form['exercise1_form']
        exercise2 = request.form['exercise2_form']
        focus = request.form['focus']
        todays_wod = [exercise1,exercise2]
        warmups_compiled = get_warmups_compiled(intensity,todays_wod,focus)

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
