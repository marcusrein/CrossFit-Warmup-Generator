import warmups_dataset
import exercises_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request
app = Flask(__name__)

##THE THING IN QUOTES IS THE KEY
## ACTION = IN THE HTML FILE AUTOMATICALLY GOES TO THE NEXT ROUTE!!! FUCCCKKKK


time_prompt = 0

@app.route('/', methods=['GET', 'POST'])
def first_page():
    global time_prompt
    if request.method == 'POST':
        print('postmethodfired$$$$$$$$$$$$$$$$$$$$$$$')
        time_prompt = request.form['time_prompt_form']
        # time_prompt = request.args.get('time')
        print(time_prompt)

        return render_template('get_exercises.html', time_prompt=time_prompt)

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