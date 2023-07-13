from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField('Click me to start your test')

class QuestionsFormEasy(FlaskForm):
    question_1 = StringField("Question 1", validators=[DataRequired()])
    question_2 = StringField("Question 2", validators=[DataRequired()])
    submit = SubmitField('Submit Answers')

class QuestionsFormHard(FlaskForm):
    question_1 = StringField("Question 1", validators=[DataRequired()])
    question_2 = StringField("Question 2", validators=[DataRequired()])
    submit = SubmitField('Submit Answers')