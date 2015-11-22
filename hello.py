from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host="192.168.1.83",port=5000)

