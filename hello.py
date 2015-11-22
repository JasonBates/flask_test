from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def default():
    return "hello world test"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "user name is %s " % request.values['username']
    else:
        return "<form method ='post' action='/login'><input type='text' \
            name='username'> <p><button type='submit'>submit</button>"

if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.1.85", port=5000)
