from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods= ['POST'])
def quiz():
    country_name=request.form['country']
    user_answer=request.form['answer']
    country_data = get_country_data(country_name)
    
    if country_data:
        correct_answer=country_data.get('capital')
        if user_answer.lower()==correct_answer.lower():
            feedback='Correct!'
        else:
            feedback=f'Incorrect! The correct answer is {correct_answer}.'
        return render_template('quiz.html', country=country_data, feedback=feedback)
    else:
        return render_template('error.html')

def get_country_data(country_name):
    response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}?fields=capital, currencies, region')
    if response.status_code==200:
        data = response.json()
        if data and isinstance(data, list):
            country= data[0]
            return country
    return None

if __name__ == '__main__':
    app.run(debug=True)


