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
        username = username + ' ' + surname
    elif username and not surname:
        username = username
    elif surname and not username:
        username = surname
    else:
        username = 'World'
    return render_template('index2.html', username=username)


@app.route('/iterate')
def iterate():
    username = request.args.get('username')
    no_of_times = request.args.get('no_of_times')

    # Checks if no_of_times is empty, negative, or zero value, then defaults to 1
    if not no_of_times or no_of_times.isdigit() is False:
        no_of_times = 1

    # Split username into names if applicable,capitalize names, and convert list of names to string
    username = " ".join(names.capitalize() for names in username.split())

    return render_template('index3.html', username=username, no_of_times=int(no_of_times))


if __name__ == '__main__':
    app.run(debug=True)
