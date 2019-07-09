from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	prediction = regressor.predict([[1, 0, 0]]).round(1)
	prediction = str(prediction)
	return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
	model = joblib.load('regressor.pkl')
	app.run(debug=True)