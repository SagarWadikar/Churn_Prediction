# Bank Customer Churn Prediction

## Introduction

Bank customer churn occurs when a customer closes their account or stops using a bank's products or services. This repository focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to churn in order to take proactive measures and retain them.

## Project Flow

The project follows the following flow:

1. **Problem Statement**: The problem is defined as the bank experiencing a higher churn rate compared to the industry average. The goal is to develop a model that can predict customers most likely to churn, enabling targeted retention efforts.

2. **Data Gathering**: The necessary data is collected, which includes features such as credit score, region, estimated salary, gender, age, balance, number of bank products used, tenure, credit card usage, and active membership.

3. **Data Preprocessing and EDA**: The collected data is preprocessed and explored through exploratory data analysis (EDA) techniques. This involves handling missing values, encoding categorical variables, and examining relationships between variables.

4. **Feature Engineering**: Additional features are created or extracted from the existing dataset to enhance the predictive power of the model. This step involves transforming and combining existing features or creating new features based on domain knowledge.

5. **Feature Selection/Extraction**: The most relevant features for predicting customer churn are selected or extracted. This helps reduce dimensionality and focuses on the most informative aspects of the data.

6. **Model Training**: Machine learning models, such as logistic regression and K-nearest neighbors (KNN), are trained on the preprocessed data. These models learn patterns and relationships in the data to make predictions.

7. **Model Evaluation**: The trained models are evaluated using various performance metrics, including accuracy, precision, recall, F1-score, confusion matrix, and ROC curve. This assessment helps gauge the effectiveness of the models in predicting customer churn.

8. **Web Development Framework**: An API is developed using Flask, a web development framework in Python. This allows the trained model to be deployed and accessed through a web interface.

9. **Deployment to Cloud Platforms**: The Flask application, along with the trained model, is deployed to a cloud platform, such as an AWS EC2 instance. This enables the application to be accessible online.

## Requirements

To run the code in this repository, the following requirements are needed:

- Flask==2.3.2
- numpy==1.23.5
- pandas==1.5.3
- scikit-learn==1.2.2
- plotly==5.14.1
- seaborn==0.12.2
- Python 3.11.4
- Jupyter Notebook (for running the code)

To install the required Python packages, run: pip install -r requirements.txt

## Usage

1. Clone this repository: git clone https://github.com/SagarWadikar/churn_prediction.git
2. Navigate to the project directory: cd churn_prediction
3. Run the Jupyter Notebook: jupyter notebook
4. Open the `Churn_Prediction.ipynb` notebook in your browser.
5. Follow the instructions in the notebook to preprocess the data, train the machine learning models, and evaluate their performance.

## Web Development and Deployment

- The Flask application is created with the necessary routes and functions to serve the churn prediction model as an API.
- Configuration for web development is handled using Flask.
- The application can be deployed to a cloud platform, such as an AWS EC2 instance, to make it accessible online.

## Usage of the API

To make predictions using the churn prediction model, you can utilize the Flask API that has been developed. Follow the steps below to use the API:

1. Ensure that you have installed the required Python packages mentioned in the "Requirements" section of this README.

2. Run the Flask application by executing command in the terminal: python3 interface.py
   
3. Once the Flask application is running, you can interact with the API using HTTP requests. The API provides the following endpoint:

- **Endpoint**: `/predict_churn`
- **Method**: POST
- **Input**: JSON object containing customer information (e.g., credit score, age, balance, etc.)
- **Output**: JSON object containing the churn prediction result (1 for churn, 0 for non-churn)

## References

- [Kaggle: Bank Customer Churn Prediction](https://www.kaggle.com/code/nasirislamsujan/bank-customer-churn-prediction)






