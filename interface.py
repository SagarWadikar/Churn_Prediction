from flask import Flask, request, jsonify, render_template
from utils import ChurnPrediction
import config

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route("/predict_churn", methods= ['POST'])
def predict_churn():

    data = request.form

    credit_score = int(data["credit_score"])
    gender = data["gender"]
    age = int(data["age"])
    tenure = int(data["tenure"])
    balance = float(data["balance"])
    products_number = int(data["products_number"])
    credit_card = int(data["credit_card"])
    active_member = int(data["active_member"])
    estimated_salary = float(data["estimated_salary"])
    country = data["country"]
             
    obj = ChurnPrediction(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
             
    pred_churn = obj.get_predicted_churn()
            
    return render_template('index.html', prediction = pred_churn)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUMBER, debug=False)





#              # if request.method == 'GET':
#         #     data = request.args.get
            
#         #     credit_score = int(data["credit_score"])
#         #     gender = data("gender")
#         #     age = int(data["age"])
#         #     tenure = int(data("tenure"))
#         #     balance = float(data("balance"))
#         #     products_number = int(data("products_number"))
#         #     credit_card = int(data("credit_card"))
#         #     active_member = int(data("active_member"))
#         #     estimated_salary = float(data("estimated_salary"))
#         #     country = data("country")

#         #     obj = ChurnPrediction(credit_score,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,country)
#         #     pred_churn = obj.get_predicted_churn()

#         #     return jsonify({"Result":f"Predicted customer churn == {pred_churn}"})
        
#         # elif request.method == 'POST':
#         #     data = request.form.get
#         #     print("Data :",data)

#         #     credit_score = int(data["credit_score"])
#         #     gender = data("gender")
#         #     age = int(data("age"))
#         #     tenure = int(data("tenure"))
#         #     balance = float(data("balance"))
#         #     products_number = int(data("products_number"))
#         #     credit_card = int(data("credit_card"))
#         #     active_member = int(data("active_member"))
#         #     estimated_salary = float(data("estimated_salary"))
#         #     country = data("country")

# credit_score = int(data("credit_score", 0))
#             gender = int(data("gender",'0'))
#             age = int(data("age", 0))
#             tenure = int(data("tenure", 0))
#             balance = float(data("balance", 0.0))
#             products_number = int(data("products_number", 0))
#             credit_card = int(data("credit_card", 0))
#             active_member = int(data("active_member", 0))
#             estimated_salary = float(data("estimated_salary", 0.0))
#             # country = data("country")
#             country = data.get("country", "")
