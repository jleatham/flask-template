from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SelectField, SubmitField
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

class archWeekForm(FlaskForm):
    #architecture  =	SelectField('Architecture', choices=[('EN','Enterprise Networking'),('SEC','Security'),('DC','Data Center'),('COLLAB','Collaboration'),('APP','Applications / Other')], validators=[DataRequired()])
    internal	  = RadioField('Internal?', choices=[('internal','Internal'),('external','External')], validators=[DataRequired()]) 
    category	  = SelectField('Category', choices=[('news','News'),('demo','Demonstrations'),('services','Services / AS'),('spiff','SPIFFs'),('capital','Capital'),('ea','EA'),('proposal','Unsolicitad BoMs / Proposals'),('promo','Product Promotions')], validators=[DataRequired()])
    bullet	      = StringField('Main Bullet', validators=[DataRequired()])
    bLink	      = StringField('URL or Box link, if any')
    subBullet1	  = StringField('Sub Bullet, if any')
    sb1Link	      = StringField('URL or Box link, if any')
    subBullet2	  = StringField('Sub Bullet, if any')
    sb2Link	      = StringField('URL or Box link, if any')
    subBullet3	  = StringField('Sub Bullet, if any')
    sb3Link	      = StringField('URL or Box link, if any')
    subBullet4	  = StringField('Sub Bullet, if any')
    sb4Link	      = StringField('URL or Box link, if any')
    subBullet5	  = StringField('Sub Bullet, if any')
    sb5Link       = StringField('URL or Box link, if any')
    submit        = SubmitField('Update')