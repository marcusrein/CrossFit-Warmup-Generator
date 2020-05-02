import warmups_dataset
import exercises_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    warmup1 = request.args.get['warmup']
    return warmups[warmup1]



if __name__ == '__main__':
    app.run(debug=True)