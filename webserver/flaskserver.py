### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 
import json
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager, login_user, current_user
from forms import LoginForm, RegistrationForm, BlogForm, MatchForm, SearchForm
from loginmanagement import getUserbyID, getUserbyName
import sqlite3
from matchingActivity import getMatch

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
        print(user)
        if not user:
            flash(f'Incorrect Username')
        elif form.password.data != user.userPassword:
            flash(f'Incorrect Password')
        else:
            print(user.__dict__) 
            print("login: ", login_user(user))
            flash(f'Logged in Successfully')
            return redirect(url_for('profile'))
    return render_template('login.html', title='Login', form=form)

@app.route('/match', methods=['GET', 'POST'])
def match():
    form = MatchForm()
    if form.validate_on_submit():

        # this is the query called NANI 
        result = getMatch(form.preferredPosition.data, form.rankRangeBot.data, form.rankRangeTop, form.queType.data)
        #result = getMatchedUserInfo(form.)
        print("test")
        print(result)
        if not result:
            flash(f'failed')
        else:    
            flash(f'succesffuly matched')
            print("match type result:")
            print(type(result))
            return redirect(url_for('matchingPage', result = result))
    return render_template('match.html', title='Match', form=form)


@app.route("/matchingPage", methods=['GET', 'POST'])
def matchingPage():
    var = request.args.getlist('result')
    print(type(var))
    print(var)
    print(type(var[0]))
    for i in range(len(var)):
        var[i] = var[i].replace("\'", '\"')
        var[i] = json.loads(var[i])

    return render_template('matchingPage.html', result = var, title = "matchingPage")

@app.route("/searchPage", methods=['GET', 'POST'])
def searchPage():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('searchedResult'))
        
    return render_template('searchPage.html', title='Search', form=form)

@app.route("/searchedResult",  methods=['GET', 'POST'])
def searchedResult():
    return render_template('searchedResult.html', title='Search Result')

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

