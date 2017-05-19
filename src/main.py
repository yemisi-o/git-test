from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/profile')
def profile():
    username = request.args.get('username')
    surname = request.args.get('surname')
    # Condition to check for username and/or surname
    if username and surname:
        username = '{} {}'.format(username, surname)
    elif username and not surname:
        username = username
    elif surname and not username:
        username = surname
    else:
        username = 'World'
    return render_template('index2.html', username=username)


@app.route('/iterate')
def iterate():
    username = request.args.get('username', default="")
    surname = request.args.get('surname', default="")
    no_of_times = request.args.get('no_of_times')

    if not(username or surname):
        username = 'World'

    username = '{} {}'.format(username.capitalize(), surname.capitalize())

    if not no_of_times or no_of_times.isdigit() is False:
        no_of_times = 1

    return render_template('index3.html', username=username, no_of_times=int(no_of_times))


if __name__ == '__main__':
    app.run(debug=True)
