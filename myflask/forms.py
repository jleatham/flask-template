from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SelectField SubmitField
from wtforms.validators import DataRequired

#Could possibly use Marshmallow to create schema, but is not built for forms so 
#would need some more code.
#I think the purpose of it is to accept either json or a dictionary and
#convert back and forth with a schema class that can be used as often as needed


class LoginForm(FlaskForm):
    testField   = StringField('testField')
    username    = StringField('Username Label', validators=[DataRequired()])
    password    = PasswordField('Password', validators=[DataRequired()])
    radioExample     = RadioField('Label', choices=[('value','value description'),('value_two','value_two description'),('value_three','value_three description')])
    selectExample   = SelectField('Select Dropdown Label', choices=[('EN','Enterprise Networking'),('SEC','Security'),('DC','Data Center')])
    remember_me = BooleanField('Remember Me')
    submit      = SubmitField('Sign In')
