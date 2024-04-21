from flask import Flask, render_template, jsonify, request
import joblib
import numpy as np
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    data = request.json
    gender = 1 if data.get("gender") == "male" else 0
    age = int(data.get("age"))
    salary = float(data.get("salary"))

    model = joblib.load("best_model.joblib")
    input_array = np.array([gender,age,salary])
    print(np.expand_dims(input_array, axis=0))
    prediction = model.predict(np.expand_dims(input_array, axis=0))
    if prediction[0] == 1:
        return "Purchase"
    else:
        return "Non Purchase"


if __name__ == "__main__":
    app.run(debug=True)