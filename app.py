from flask import Flask, render_template, request, url_for
import pywhatkit


app = Flask(__name__)




@app.route('/')
def home():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def main():
	if request.method == 'POST':
		text = str(request.form['tex'])
		pywhatkit.text_to_handwriting(text, rgb=(0,0,0))
		return render_template("success.html")
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug = True)

