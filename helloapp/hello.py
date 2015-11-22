from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def default():
    return "hello world test"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       return "User %s logged in" % request.form['username']
    return render_template('login.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.1.85", port=5000)
