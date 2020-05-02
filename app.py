import warmups_dataset
import exercises_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    exercise1 = request.args.get('exercise_1')
    exercise2 = request.args.get('exercise_2')
    return '''<h4>The first exercise is {}<h4>
    <h4>The second exercise is {}<h4>'''.format(exercises[exercise1], exercises[exercise2])

if __name__ == '__main__':
    app.run(debug=True)