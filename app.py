## Meditate on this
## Fill out more dummy functions to make them actually work
## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)

import warmups_dataset
import exercises_dataset

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
    optimal_warmup_time = get_optimal_warmup_time(intensity,has_loaded_exercise,has_kb_exercise,has_barbell_exercise)

    return {'optimal_warmup_time':optimal_warmup_time,'intensity':intensity,'todays_wod':todays_wod,'has_loaded_exercise':has_loaded_exercise,'has_kb_exercise':has_kb_exercise,'has_barbell_exercise':has_barbell_exercise,'focus':focus}
    ## line32: if i have more processing to do, maybe make another function (get_best_warmups_EVER to summarize, return, print it)


def check_loaded_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == False:
            return False
        else:
            return True

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

def get_optimal_warmup_time(intensity,has_loaded_exercise,has_kb_exercise,has_barbell_exercise):
    ### DUMMY FUNC
    return 30


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

@app.route('/', methods=['GET', 'POST'])
def first_page():
    if request.method == 'POST':
        exercise1 = request.form['exercise1_form']
        exercise2 = request.form['exercise2_form']
        intensity = request.form['intensity_form']
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
