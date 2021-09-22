from  flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,Length,DataRequired,EqualTo

#Create a form class
class RegisterForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16)])
    confirm = PasswordField('Confirm-Password',validators=[DataRequired(), EqualTo('password')])
    signup = SubmitField('SignUp')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16)])
    signin = SubmitField('SignIn')