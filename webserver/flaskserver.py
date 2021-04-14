### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 

from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager, login_user, current_user
from forms import LoginForm, RegistrationForm, BlogForm, MatchForm
from loginmanagement import getUserbyID, getUserbyName
import sqlite3
from matchingActivity import getPositionbyInp

conn = sqlite3.connect('leaguemate.db')
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#manage logged in users
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    user = getUserbyID(id)
    return user

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

######## Route URLS ###################

@app.route("/")
@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/login", methods=['GET', 'POST'])
def login():   
    form = LoginForm()

    if form.validate_on_submit():
        user = getUserbyName(form.username.data)
        if not user:
            flash(f'Incorrect Username')
        elif form.password.data != user.userPassword:
            flash(f'Incorrect Password')
        else:
            print("login: ", login_user(user))
            flash(f'Logged in Successfully')
            return redirect(url_for('profile'))
    return render_template('login.html', title='Login', form=form)

@app.route('/match', methods=['GET', 'POST'])
def match():
    form = MatchForm()
    if form.validate_on_submit():
        
        user = getPositionbyInp(form.preferredPosition.data, current_user.id)

        if not user:
            flash(f'failed')
        else:    
            login_user(user)
            flash(f'succesffuly matched')
            flash(current_user.matchedLeagueid)
            return redirect(url_for('matchingPage'))
    return render_template('match.html', title='Match', form=form)


@app.route("/matchingPage")
def matchingPage():       
    return render_template('matchingPage.html')

@app.route("/debug")
def debug():
    print("auth: ",current_user, current_user.is_authenticated)
    return render_template('layout.html', title='Login')
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()

#     if form.validate_on_submit():
#         conn = sqlite3.connect('blog.db')
#         c = conn.cursor()
        
#         #Add the new blog into the 'blogs' table
#         query = 'insert into users VALUES (?, ?, ?)'
#         c.execute(query, (form.username.data, form.email.data, form.password.data)) #Execute the query
#         conn.commit() #Commit the changes

#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @app.route("/blog", methods=['GET', 'POST'])
# def blog():
#     conn = sqlite3.connect('blog.db')

#     #Display all usernames stored in 'users' in the Username field
#     conn.row_factory = lambda cursor, row: row[0]
#     c = conn.cursor()
#     c.execute("SELECT username FROM users")
#     results = c.fetchall()
#     users = [(results.index(item), item) for item in results]

#     form = BlogForm()
#     form.username.choices = users

#     if form.validate_on_submit():
#         choices = form.username.choices
#         user =  (choices[form.username.data][1])
#         title = form.title.data
#         content = form.content.data

#         #Add the new blog into the 'blogs' table in the database
#         query = 'insert into blogs (username, title, content) VALUES (?, ?, ?)' #Build the query
#         c.execute(query, (user, title, content)) #Execute the query
#         conn.commit() #Commit the changes

#         flash(f'Blog created for {user}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('blog.html', title='Blog', form=form)

if __name__ == '__main__':
    app.run(debug=True,port=7000)

