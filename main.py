from flask import Flask, render_template, request
from algo.slurp import correct

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/correct', methods=['POST'])
def return_correction():
	corrected_word = correct(request.form['correct'])
	return render_template('index.html', corrected_word=corrected_word)

@app.errorhandler(404)
def page_not_found(e):
	"""Return a custom 404 error."""
	return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
	"""Return a custom 500 error."""
	return 'Sorry, unexpected error: {}'.format(e), 500

if __name__=="__main__":
	app.run()
