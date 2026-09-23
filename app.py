from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "student_performance.csv"
MODEL_PATH = BASE / "models" / "student_performance_model.joblib"

app = Flask(__name__)
df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

def risk_label(score):
    if score < 8:
        return "High Risk"
    if score < 11:
        return "Moderate Risk"
    return "Lower Risk"

@app.route("/")
def home():
    summary = {
        "students": int(len(df)),
        "avg_grade": round(float(df["G3"].mean()), 2),
        "avg_absences": round(float(df["absences"].mean()), 2),
        "pass_rate": round(float((df["G3"] >= 10).mean() * 100), 1),
    }
    return render_template("index.html", summary=summary)

@app.route("/predict", methods=["POST"])
def predict():
    form = request.form
    row = {
        "school": form["school"],
        "sex": form["sex"],
        "age": int(form["age"]),
        "address": form["address"],
        "famsize": form["famsize"],
        "studytime": int(form["studytime"]),
        "failures": int(form["failures"]),
        "schoolsup": form["schoolsup"],
        "famsup": form["famsup"],
        "paid": form["paid"],
        "activities": form["activities"],
        "higher": form["higher"],
        "internet": form["internet"],
        "famrel": int(form["famrel"]),
        "freetime": int(form["freetime"]),
        "goout": int(form["goout"]),
        "health": int(form["health"]),
        "absences": int(form["absences"]),
        "G1": int(form["G1"]),
        "G2": int(form["G2"]),
    }
    sample = pd.DataFrame([row])
    score = float(model.predict(sample)[0])
    score = max(0, min(20, score))
    return render_template("index.html",
                           summary={
                               "students": int(len(df)),
                               "avg_grade": round(float(df["G3"].mean()), 2),
                               "avg_absences": round(float(df["absences"].mean()), 2),
                               "pass_rate": round(float((df["G3"] >= 10).mean() * 100), 1),
                           },
                           prediction=round(score, 2),
                           risk=risk_label(score))

@app.route("/api/summary")
def api_summary():
    return jsonify({
        "students": int(len(df)),
        "avg_grade": round(float(df["G3"].mean()), 2),
        "avg_absences": round(float(df["absences"].mean()), 2),
        "pass_rate": round(float((df["G3"] >= 10).mean() * 100), 1)
    })

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
