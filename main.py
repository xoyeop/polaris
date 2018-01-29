from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def search():
	keyword = request.form['keyword']
	return render_template('result.html', keyword=keyword)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
