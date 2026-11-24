
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib
import sqlite3
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "purchase_prediction_model.joblib"
DATABASE_PATH = BASE_DIR / "prediction_history.db"

# Load trained ML model
saved_model = joblib.load(MODEL_PATH)

model = saved_model["model"]
threshold = saved_model["threshold"]


# ------------------------------------------------
# DATABASE INITIALIZATION
# ------------------------------------------------

def initialize_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prediction_date TEXT,
            prediction TEXT,
            probability REAL,
            month TEXT,
            visitor_type TEXT
        )
    """)

    connection.commit()
    connection.close()


# ------------------------------------------------
# SAVE PREDICTION
# ------------------------------------------------

def save_prediction(prediction, probability, month, visitor_type):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (prediction_date, prediction, probability, month, visitor_type)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        prediction,
        probability,
        month,
        visitor_type
    ))

    connection.commit()
    connection.close()


# ------------------------------------------------
# FETCH PREDICTION HISTORY
# ------------------------------------------------

def get_prediction_history():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM predictions
        ORDER BY id DESC
        LIMIT 20
    """)

    history = cursor.fetchall()

    cursor.execute("""
        SELECT COUNT(*) FROM predictions
    """)

    total_predictions = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM predictions
        WHERE prediction = 'Purchase Likely'
    """)

    likely_purchases = cursor.fetchone()[0]

    connection.close()

    return history, total_predictions, likely_purchases


# ------------------------------------------------
# HOME PAGE
# ------------------------------------------------


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    probability = None
    error = None

    if request.method == "POST":

        try:

            input_data = {
                "Administrative": int(request.form["Administrative"]),
                "Administrative_Duration": float(request.form["Administrative_Duration"]),
                "Informational": int(request.form["Informational"]),
                "Informational_Duration": float(request.form["Informational_Duration"]),
                "ProductRelated": int(request.form["ProductRelated"]),
                "ProductRelated_Duration": float(request.form["ProductRelated_Duration"]),
                "BounceRates": float(request.form["BounceRates"]),
                "ExitRates": float(request.form["ExitRates"]),
                "SpecialDay": float(request.form["SpecialDay"]),
                "Month": request.form["Month"],
                "OperatingSystems": int(request.form["OperatingSystems"]),
                "Browser": int(request.form["Browser"]),
                "Region": int(request.form["Region"]),
                "TrafficType": int(request.form["TrafficType"]),
                "VisitorType": request.form["VisitorType"],
                "Weekend": request.form["Weekend"] == "True"
            }

            input_df = pd.DataFrame([input_data])

            probability_value = model.predict_proba(input_df)[0][1]

            if probability_value >= threshold:
                prediction = "Purchase Likely"
            else:
                prediction = "Purchase Unlikely"

            probability = round(probability_value * 100, 2)

            # Save prediction exactly once
            save_prediction(
                prediction,
                probability,
                input_data["Month"],
                input_data["VisitorType"]
            )

            # Redirect to GET request after saving
            return redirect(
                url_for(
                    "home",
                    prediction=prediction,
                    probability=probability
                )
            )

        except (ValueError, KeyError) as e:
            error = f"Invalid input: {e}"

    else:
        # Display the previous result after redirect
        prediction = request.args.get("prediction")
        probability_value = request.args.get("probability")

        if probability_value is not None:
            try:
                probability = float(probability_value)
            except ValueError:
                prediction = None
                probability = None

    # Fetch prediction history
    history, total_predictions, likely_purchases = get_prediction_history()

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        threshold=threshold,
        error=error,
        history=history,
        total_predictions=total_predictions,
        likely_purchases=likely_purchases
    )


# ------------------------------------------------
# START APPLICATION
# ------------------------------------------------


# ------------------------------------------------
# ANALYTICS DASHBOARD
# ------------------------------------------------

@app.route("/dashboard")
def dashboard():

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Total predictions
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM predictions
    """)
    total = cursor.fetchone()["total"]

    # Predictions grouped by result
    cursor.execute("""
        SELECT prediction, COUNT(*) AS count
        FROM predictions
        GROUP BY prediction
    """)
    prediction_rows = cursor.fetchall()

    prediction_labels = [
        row["prediction"] for row in prediction_rows
    ]

    prediction_counts = [
        row["count"] for row in prediction_rows
    ]

    # Monthly prediction activity
    cursor.execute("""
        SELECT month, COUNT(*) AS count
        FROM predictions
        GROUP BY month
        ORDER BY
            CASE month
                WHEN 'Feb' THEN 1
                WHEN 'Mar' THEN 2
                WHEN 'May' THEN 3
                WHEN 'June' THEN 4
                WHEN 'Jul' THEN 5
                WHEN 'Aug' THEN 6
                WHEN 'Sep' THEN 7
                WHEN 'Oct' THEN 8
                WHEN 'Nov' THEN 9
                WHEN 'Dec' THEN 10
                ELSE 11
            END
    """)
    monthly_rows = cursor.fetchall()

    month_labels = [
        row["month"] for row in monthly_rows
    ]

    month_counts = [
        row["count"] for row in monthly_rows
    ]

    # Visitor type breakdown
    cursor.execute("""
        SELECT visitor_type, COUNT(*) AS count
        FROM predictions
        GROUP BY visitor_type
    """)
    visitor_rows = cursor.fetchall()

    visitor_labels = [
        row["visitor_type"] for row in visitor_rows
    ]

    visitor_counts = [
        row["count"] for row in visitor_rows
    ]

    connection.close()

    likely_purchases = sum(
        row["count"]
        for row in prediction_rows
        if row["prediction"] == "Purchase Likely"
    )

    return render_template(
        "dashboard.html",
        total=total,
        likely_purchases=likely_purchases,
        prediction_labels=prediction_labels,
        prediction_counts=prediction_counts,
        month_labels=month_labels,
        month_counts=month_counts,
        visitor_labels=visitor_labels,
        visitor_counts=visitor_counts
    )


initialize_database()

if __name__ == "__main__":
    app.run(debug=True)
