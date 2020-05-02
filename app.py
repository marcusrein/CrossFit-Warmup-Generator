import warmups_dataset
import exercises_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request
app = Flask(__name__)

todays_wod = []
@app.route('/')
def query_example():
    exercise1 = request.args.get('exercise_1')
    exercise2 = request.args.get('exercise_2')
    todays_wod.append(exercise1)
    todays_wod.append(exercise2)
    return '''<h4> Todays WOD is: {}<h4>'''.format(todays_wod)


@app.route('/form', methods=['GET','POST'])
def form_example():
    exercise1 = request.args.get('exercise_1')
    exercise2 = request.args.get('exercise_2')
    return '''<form method="POST">
                Exercise 1: <input type="text" name="exercise_2"><br>
                Exercise 2: <input type="text" name="exercise_2"><br>
                <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)