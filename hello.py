from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
	return render_template('hello.html', name=name)

@app.route('/abc')
def abc():
	return 'abv!'

if __name__ == '__main__':
	app.run(host='0.0.0.0')
