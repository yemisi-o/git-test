from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/if')
def profile():
    username = request.args.get('username')
    surname = request.args.get('surname')
    if username and surname:
        username = username + ' ' + surname
    elif username and not surname:
        username = username
    elif surname and not username:
        username = surname
    else:
        username = 'World'
    return render_template('index2.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
