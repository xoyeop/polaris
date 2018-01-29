from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def search():
	keyword = request.form['keyword']
	return render_template('result.html', keyword=keyword)

@app.route('/trajectory')
def trajectory():
	return "<h1 style='color:red'>trajectory result</h1>"

@app.route('/sentiment')
def sentiment():
	return "<h1 style='color:blue'>sentiment result</h1>"

@app.route('/semantic')
def semantic():
	return "<h1 style='color:orange'>semantic result</h1>"

@app.route("/event_detection")
def event():
	return "<h1 style='color:green'>event_detection result</h1>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
