### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 

from flask import Flask, render_template, url_for, flash, redirect, request
from forms import LoginForm, RegistrationForm, BlogForm
from loginmanagement import getUser
import sqlite3

conn = sqlite3.connect('leaguemate.db')
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route("/")
@app.route("/profile")
def profile():
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    
    username = request.args.get('username')
    userdata = None
    if username:
        query = "SELECT * from UserAccount where userName=(?)"
        c.execute(query, (username,))
        userdata = c.fetchall()

        print(f"username: {username}, data: {userdata}")
    return render_template('profile.html', userdata=userdata )

@app.route("/login", methods=['GET', 'POST'])
def login():   
    form = LoginForm()

    if form.validate_on_submit():
        conn = sqlite3.connect('leaguemate.db')
        c = conn.cursor()

        #check database for user account
        query = "SELECT userName from UserAccount where userName=(?)"
        c.execute(query, (form.username.data,))
        
        conn.commit()
        results = c.fetchall()
        print(f"results: {results}")
        if len(results) == 0:
            flash(f'Incorrect Username')
        else:
            flash(f'Logged in Successfully')
            return redirect(url_for('profile', username=results[0]))
    return render_template('login.html', title='Login', form=form)

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

