from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#DataRequired makes sure you enter something

class RegistrationForm(FlaskForm):
    username        =  StringField('Username',
                                    validators=[DataRequired(), Length(min=2, max=20)])
    email           =  StringField('Email',
                                    validators=[DataRequired(), Email()])
    password        =  PasswordField('Password',
                                    validators=[DataRequired(), Length(min=6)])
    confirmpassword =  PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    #note: choose user of mail
    username    =  StringField('Username',
                                validators=[DataRequired(), Length(min=2, max=20)])
    email       =  StringField('Email',
                                validators=[DataRequired(), Email()])
    password    =  PasswordField('Password',
                                validators=[DataRequired(), Length(min=6)])
    remember    = BooleanField('Remember Me')
    
    submit = SubmitField('Log in')