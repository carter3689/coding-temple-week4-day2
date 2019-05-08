from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo

class PostForm(FlaskForm):
    title = StringField("What will your title say?",validators=[DataRequired()])
    post = StringField("What is on your mind?", validators=[DataRequired()])
    submit = SubmitField("Send Tweet")