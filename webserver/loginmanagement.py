from flask_login import LoginManager, UserMixin
import sqlite3

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#inherit basic flask_login user properties
class User(UserMixin):
    id = None
    email = None
    userName = None
    DateOfBirth = None
    gameServer = None
    password = None
    leagueID = None

def getUser(id):
    conn = sqlite3.connect('leaguemate.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    query = "SELECT * from UserAccount where userID=(?)"
    c.execute(query, (id,))
    userdata = c.fetchall()
    if(userdata):
        user = User()
        user.id = id
        user.email = userdata[0]['email']
        user.userName = userdata[0]['userName']
        user.DateOfBirth = userdata[0]['dateOfBirth']
        user.gameServer = userdata[0]['gameServer']
        user.userPassword = userdata[0]['userPassword']
        user.leagueID = userdata[0]['leagueID']
        return user
    else:
        return None

def MakeLoginManager(app):
    login = LoginManager()
    login.init_app(app)

    @login.user_loader
    def load_user(id):
        return getUser(id)


