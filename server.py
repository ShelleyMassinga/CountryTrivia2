from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/test/<name>', methods=['GET'])
def levels(name):
    difficulty = ['Easy', 'Medium', 'Difficult']
    return render_template("quiz.html", difficulty = difficulty)


if __name__ == "__main__":
    app.run(debug=True)