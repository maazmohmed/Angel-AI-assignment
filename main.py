from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.skillbit


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        mail = request.form['email']
        password = request.form['psw']
        pass_repeat = request.form['psw-repeat']
        dic1 = dict({'Email': mail, 'password': password, 'password-repeat': pass_repeat})
        data = db.info.insert_one(dic1)
        return "you have successfully registered yourself as a user"
    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form["uname"]
        password = request.form["psw"]
        dic = dict({'username': name, 'password': password})
        data = db.info.insert_one(dic)
        return "You have successfully logged in as" + " " + name
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
