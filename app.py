import warmups_dataset
import exercises_dataset

exercises = exercises_dataset.get_exercises()
warmups = warmups_dataset.get_warmups()
warmup_metcons = warmups_dataset.get_warmup_metcons()

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

## THE GREEN QUOTES = THE KEY!, then the = leads to the value
## requests.args.get is optional data as it comes back "none" if nothing is entered
## requests.args[' '] is nonoptional data as it will return back an error. better for critical info.
@app.route('/')
def query_example():
    todays_wod = []
    exercise1 = request.args.get('exercise_1')
    exercise2 = request.args.get('exercise_2')
    website = request.args['website']
    todays_wod.append(exercise1)
    todays_wod.append(exercise2)
    return '''<h4> Todays WOD is: {}. Todays website is {}<h4>'''.format(todays_wod, website)


##Testing out POST and GET. if request.method == ['POST']: return '<h1> asdf <h1>'
@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '<h1>The language is {}. The framework is {}.<h1>'.format(language, framework)

    return '''<form method="POST">
    Language <input type="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit">
    </form>'''

#
# def get_warmups_for_todays_wod():


# @app.route('/form', methods=['GET','POST'])
# def form_example():
#     todays_wod = []
#     exercise1 = request.args.get('exercise_1')
#     exercise2 = request.args.get('exercise_2')
#     todays_wod.append(exercise1)
#     todays_wod.append(exercise2)
#     return '''<form method="POST">
#                 Exercise 1: <input type="text" name="exercise_1"><br>
#                 Exercise 2: <input type="text" name="exercise_2"><br>
#                 <input type="submit" value="Submit"><br>
#               </form>'''

if __name__ == '__main__':
    app.run(debug=True)