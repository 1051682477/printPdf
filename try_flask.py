from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return 'Login'


@app.route('/login/for')
def login_for():
    a = 1
    lists = []
    while a < 50:
        lists.append(a)
        a += a
    return_list = str(lists)

    return return_list


def do_the_login():
    dicts = {"name": "do_the_login"}
    return jsonify(dicts)


def show_the_login_form():
    return 'show_the_login_form'


@app.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'GET':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
    app.run()
