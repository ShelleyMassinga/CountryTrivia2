from flask import Flask, render_template, flash, redirect, url_for, session
import requests
from form import QuestionsFormEasy, SignUpForm, QuestionsFormHard
from flask_behind_proxy import FlaskBehindProxy
import secrets
import database


app = Flask(__name__)
proxied = FlaskBehindProxy(app)

app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup', methods = ['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit(): # checks if entries are valid
        username = form.username.data
        session['username'] = username
        database.insert_into_user_info(username)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('test')) # if so - send to map page
    return render_template('sign_up.html', form=form)


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/test')
def test():
    username = session.get('username')
    return render_template("test.html", username=username)

@app.route('/test/<name>', methods=['GET'])
def levels(name):
    session['country_name'] = name
    difficulty = ['Easy', 'Hard']
    return render_template("difficulty.html", difficulty = difficulty)

@app.route('/test/<name>/<level>', methods= ['GET', 'POST'])
def quiz(level, name):
    session["level"] = level
    if level == "Easy":
        form = QuestionsFormEasy()
        name = session.get('country_name')
        form.question_1.label.text = f"What is the capital of {name}?"
        form.question_2.label.text = f"What continent is {name} located?"
        correct = 0
        incorrect = 0
        if form.validate_on_submit(): # checks if entries are valid
            answers = [form.question_1.data, form.question_2.data]
            country_data = get_country_data(name)
            correct_answers = [str(country_data["capital"][0]), str(country_data["region"])]
            counter = 0
            for answer in answers:
                if answer.lower() == correct_answers[counter].lower():
                    correct += 1
                else:
                    incorrect += 1
                counter += 1
                
            total=correct + incorrect
            session["total"] = total
            session["correct"] = correct
            session["incorrect"] = incorrect
            session["answer_1"] = correct_answers[0]
            session["answer_2"] = correct_answers[1]
            database.insert_into_results(session.get("username"), name, level, correct, incorrect)
            return redirect(url_for('results'))
    else:
        form = QuestionsFormHard()
        name = session.get('country_name')
        form.question_1.label.text = f"What is the national language of {name}?"
        form.question_2.label.text = f"What is the sub-region location of {name}?"
        correct = 0
        incorrect = 0
        if form.validate_on_submit(): # checks if entries are valid
            answers = [form.question_1.data, form.question_2.data]
            country_data = get_country_data(name)
            correct_answers = [str(list(country_data["languages"].values())[0]), str(country_data["subregion"])]
            print(correct_answers)
            counter = 0
            for answer in answers:
                if answer.lower() == correct_answers[counter].lower():
                    correct += 1
                else:
                    incorrect += 1
                counter += 1
            total=correct + incorrect
            session["total"] = total
            session["level"] = level
            session["correct"] = correct
            session["incorrect"] = incorrect
            session["answer_1"] = correct_answers[0]
            session["answer_2"] = correct_answers[1]
            database.insert_into_results(session.get("username"), name, level, correct, incorrect)
            return redirect(url_for('results'))
    return render_template('quiz.html', form=form)


def get_country_data(country_name):
    response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
    if response.status_code==200:
        data = response.json()
        if data and isinstance(data, list):
            country= data[0]
            return country
    return None

@app.route('/results')
def results():
    level = session.get("level")
    correct = session.get("correct")
    incorrect = session.get("incorrect")
    username = session.get("username")
    country_name = session.get("country_name")
    answer_1 = session.get("answer_1")
    answer_2 = session.get("answer_2")
    total = session.get("total")
    top_three_scores = database.top_three_correct_answers(country_name, level)
    session["top_three_scores"] = top_three_scores

    return render_template('results.html', top_three_scores=top_three_scores, total=total, level=level, correct=correct, incorrect=incorrect, username=username, country_name=country_name, answer_1=answer_1, answer_2=answer_2)

    


if __name__ == "__main__":
    app.run(debug=True)