from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField, TextAreaField, SelectField, RadioField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    accountname = StringField('Account Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProfileForm(FlaskForm):
    accountname = StringField('Accountname', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    leagueID = StringField('LeagueID', validators=[DataRequired()])

class MatchForm(FlaskForm):
    preferredPosition = SelectField('Preferred Position', choices=['Top', 'Jungle', 'Middle', 'Bottom', 'Support'])

    rankRangeBot = SelectField('Min', choices=['N/A', 'Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger'])

    rankRangeTop = SelectField('Max', choices=['N/A', 'Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger'])

    #champions = StringField('Preferred Champion', validators=[DataRequired()])

    queType = SelectField('Preferred Queue Type', choices=['AnyType', 'Solo/Duo', 'Flex', 'TFT', 'ARAM'])

    save = SubmitField('Save')

class SearchForm(FlaskForm):
    byPosition = SelectField('Preferred Position', choices=['Top', 'Jungle', 'Middle', 'Bottom', 'Support'])
    byRank = SelectField('Rank Range', choices=['N/A', 'Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Master', 'Grandmaster', 'Challenger'])
    byQueType = SelectField('Preferred Queue Type', choices=['AnyType', 'Solo/Duo', 'Flex', 'TFT', 'ARAM'])

    search = SubmitField('Search')

class RegisterForm(FlaskForm):
    accountname = StringField('Accountname', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    dateofbirth = DateField('Dateofbirth', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
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
    
    
