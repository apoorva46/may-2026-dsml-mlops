from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

# Home Page
@app.route("/", methods=["GET"])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Loan Prediction App</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #c6ff00, #d4fc79);
                color: white;
                text-align: center;
            }

            h1 {
                font-size: 50px;
                margin-bottom: 10px;
            }

            p {
                font-size: 24px;
            }

            .card {
                background: rgba(255,255,255,0.15);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🏦 Loan Prediction App</h1>
            <p>Machine Learning Powered Loan Approval Prediction</p>
            <p>Use the /predict API endpoint to get predictions.</p>
        </div>
    </body>
    </html>
    """

# Health Check Endpoint
@app.route("/ping", methods=["GET"])
def pinger():
    return {"message": "API is running successfully"}

# JSON Test Endpoint
@app.route("/json", methods=["GET"])
def json_check():
    return {"message": "Hi, I am JSON!"}

# Load Model
with open("classifier.pkl", "rb") as model_pickle:
    clf = pickle.load(model_pickle)

# Prediction Endpoint
@app.route("/predict", methods=["POST"])
def prediction():

    loan_req = request.get_json()

    if loan_req["Gender"] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req["Married"] == "Yes":
        Married = 1
    else:
        Married = 0

    ApplicantIncome = loan_req["ApplicantIncome"]
    LoanAmount = loan_req["LoanAmount"]
    Credit_History = loan_req["Credit_History"]

    result = clf.predict(
        [[
            Gender,
            Married,
            ApplicantIncome,
            LoanAmount,
            Credit_History
        ]]
    )

    if result[0] == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return {
        "loan_approval_status": pred
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)