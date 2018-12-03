from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    testField   = StringField('testField')
    username    = StringField('Username Label', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    radioExample     = RadioField('Label', choices=[('value','value description'),('value_two','value_two description'),('value_three','value_three description')])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')
