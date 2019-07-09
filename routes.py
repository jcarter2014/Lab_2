from flask import Flask, render_template
from sklearn.externals import joblib

app = Flask(__name__)
model = joblib.load('regressor.pkl')

@app.route("/")
def index():
	prediction = 497632
	prediction = str(prediction)
	return render_template("index.html", prediction = prediction)

if __name__ == "__main__":

	app.run(debug=True)