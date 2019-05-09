from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,TextAreaField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError

from app.models import User

class PostForm(FlaskForm):
    title = StringField("What will your title say?",validators=[DataRequired()])
    post = StringField("What is on your mind?", validators=[DataRequired()])
    submit = SubmitField("Send Tweet")


class LoginForm(FlaskForm):
    # email, password, remember_me, submit

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    #email, password, password2, submit
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Re-type your password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first() # This will check the email based on the first instance in the database
        if user is not None:
            raise ValidationError("Please use a different email address")