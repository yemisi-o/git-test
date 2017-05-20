from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
