### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 
import json
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from forms import LoginForm, MatchForm, SearchForm, ProfileForm, SearchSortForm
from loginmanagement import getUserbyID, getUserbyName, getUserData
import sqlite3
from matchingActivity import getMatch
from searchManagement import getAllUsers, getMaxLevel, sortUsers

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
    form = ProfileForm()
    if(current_user.is_authenticated):
        data = getUserData(["UserInfor", "UserLeague"])
        print(data)
        form.accountname = data['UserInfor'][0]['Username']
        form.email = data['UserInfor'][0]['Email']
        form.country = data['UserInfor'][0]['Country']
        form.leagueID = data['UserLeague'][0]['LeagueID']
    return render_template('profile.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():   
    form = LoginForm()
    if form.validate_on_submit():
        user = getUserbyName(form.username.data)
        if not user:
            flash(f'Incorrect Username')
        elif form.password.data != user.password:
            flash(f'Incorrect Password')
        else:
            print("login: ", login_user(user))
            flash(f'Logged in Successfully')
            return redirect(url_for('profile'))
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():   
    if(current_user.is_authenticated):
        logout_user()
        print("loggin out")
    return redirect(url_for("profile"))
    


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
        a1 =form.byPosition.data
        a2 = form.byRank.data
        a3 = form.byQueType.data
        resultdata = sortUsers(a1, a2, a3)
        if not resultdata:
            flash(f'Failed to query data')
        else:    
            flash(f'Succesffuly Queried')
            print(type(resultdata))
            return redirect(url_for('searchedResult', resultdata = resultdata, a1 = a1, a2 = a2, a3 = a3))
    return render_template('searchPage.html', title='Search', form=form)

@app.route("/searchedResult",  methods=['GET', 'POST'])
def searchedResult():
    form = SearchSortForm()
    var = request.args.getlist('resultdata')
    a1 = request.args.get('a1')
    a2 = request.args.get('a2')
    a3 = request.args.get('a3')
    print(type(var))
    print(var)
    print(type(var[0]))
    for i in range(len(var)):
        var[i] = var[i].replace("\'", '\"')
        var[i] = json.loads(var[i])
    if form.validate_on_submit():
        resultdata = getMaxLevel(a1, a2, a3)
        return(redirect(url_for('findMaxLev', resultdata=resultdata)))
    return render_template('searchedResult.html', resultdata = var, title='Search Result', form=form)

@app.route("/findMaxLev",  methods=['GET', 'POST'])
def findMaxLev():
    var = request.args.getlist('resultdata')
    for i in range(len(var)):
        var[i] = var[i].replace("\'", '\"')
        var[i] = json.loads(var[i])
    return render_template('findMaxLev.html', resultdata = var, title='Sorted Result')

@app.route("/debug")
def debug():
    print("auth: ",current_user, current_user.is_authenticated)
    return render_template('layout.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True,port=7000)

