from flask import Flask, url_for
app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    return "name " + username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "post " + str(post_id)

@app.route('/')
def show_url_for():
    return url_for('show_user_profile', username = 'Jason')

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.1.83",port=5000)

