from flask import Flask, request, jsonify, render_template, redirect, url_for
import numpy as np
from utils import ChurnPrediction
import traceback
import config

app = Flask(__name__)

@app.route("/churn_prediction")
def home():
    
    return render_template('index.html')

@app.route("/predict_churn", methods=['GET', 'POST'])
def predict_churn():
    try:
        if request.method == 'GET':
            data = request.args.get
            
            credit_score = float(data("credit_score"))
            gender = data("gender")
            age = int(data("age"))
            tenure = int(data("tenure"))
            balance = float(data("balance"))
            products_number = int(data("products_number"))
            credit_card = int(data("credit_card"))
            active_member = int(data("active_member"))
            estimated_salary = float(data("estimated_salary"))
            country = data("country")

            obj = ChurnPrediction(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
            pred_churn = obj.get_predicted_churn()

            return jsonify({"Result":f"Predicted customer churn == {pred_churn}"})
        
        elif request.method == 'POST':
            data = request.form.get
            print("Data :",data)

            credit_score = float(data("credit_score"))
            gender = data("gender")
            age = int(data("age"))
            tenure = int(data("tenure"))
            balance = float(data("balance"))
            products_number = int(data("products_number"))
            credit_card = int(data("credit_card"))
            active_member = int(data("active_member"))
            estimated_salary = float(data("estimated_salary"))
            country = data("country")

            obj = ChurnPrediction(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
            pred_churn = obj.get_predicted_churn()
            
            return render_template('index.html', prediction = pred_churn)

    except:
        print(traceback.print_exc())
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)
