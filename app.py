from flask import Flask, render_template, request, session, redirect, url_for

from datetime import timedelta 

import logging
logging.basicConfig(level=logging.INFO)

import json

with open('questions/questions.json', 'r', encoding='utf-8') as file:
    all_data = json.load(file)


questions = [question["question"] for question in all_data['questions']]
 
# logging.info(questions)

additional_questions = [question.get("additional_question", "") for question in all_data['questions']]

# logging.info(additional_questions)

#Конфигугрирование
app = Flask(__name__)
app.secret_key = 'abcdefg' # для установки session
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/', methods = ["GET", "POST"])

def auth():
    if request.method == 'POST':
        name = request.form.get('name', "")
        surname = request.form.get('surname', "")
        if name:
            session["name"] = name
        if surname:
            session["surname"] = surname
        # logging.info(name)
        # logging.info(surname)
        return redirect(url_for('start'))
    return render_template('auth.html')

@app.route('/start', methods = ["GET", "POST"])
def start():
    name = session.get('name', "")
    surname = session.get('surname', "")
    if request.method == 'POST':
        if surname == "":
            surname = request.form.get('surname')
        age = request.form.get('age')
        city = request.form.get('city')
        met_already = request.form.get('met_already')
        if surname:
            session["surname"] = surname
        if age:
            session["age"] = age
        if city:
            session["city"] = city
        if met_already:
            session["met_already"] = True
        return redirect(url_for('question'))
    return render_template('start.html', name = name, surname = surname)

@app.route('/question', methods = ["GET", "POST"])
def question():
    name = session.get("name")
    surname = session.get("surname", "")
    age = session.get("age")
    city = session.get("city", None)
    return render_template('question.html', name=name, surname=surname, age=age, city=city)


if __name__ == "__main__":
    app.run(debug=True)