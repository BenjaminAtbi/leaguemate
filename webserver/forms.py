from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MatchForm(FlaskForm):
    preferredPosition = SelectField('Preferred Position', choices=['Controller', 'Fighter', 'Mage', 'Marksman', 'Slayer', 'Specialist', 'Tank'])

    rankRange = SelectField('Rank Range', choices=['N/A', 'Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger'])

    champions = StringField('Preferred Champion', validators=[DataRequired()])

    save = SubmitField('Save')


###############
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class BlogForm(FlaskForm):
    username = SelectField('Username', choices=[], coerce=int)
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    
