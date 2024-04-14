# Bank Customer Churn Prediction Project

This project focuses on predicting bank customer churn using machine learning techniques. The goal is to develop a model that accurately identifies customers at risk of churn, enabling proactive retention strategies to be implemented by financial institutions.

## Project Overview

The model utilizes a dataset containing the following columns: 'Total_Trans_Amt', 'Total_Amt_Chng_Q4_Q1', 'Total_Ct_Chng_Q4_Q1', 'Total_Trans_Ct', 'Total_Revolving_Bal', 'Customer_Age', 'Credit_Limit', 'Total_Relationship_Count'. These features were selected based on their relevance to predicting churn behavior.

## Steps Taken

1. **Data Collection and Exploration**: The dataset was gathered and analyzed to understand the distribution of features and identify potential relationships between variables.

2. **Feature Engineering**: Relevant features were selected and engineered to enhance the predictive power of the model. This involved transforming and scaling the data to prepare it for modeling.

3. **Model Development**: Various machine learning algorithms were trained and evaluated using techniques such as cross-validation to select the most suitable model.The Random Forest algorithm was chosen for its ability to handle complex datasets and provide accurate predictions. The model was trained and evaluated using techniques such as cross-validation to ensure robust performance.

4. **Model Deployment**:  The trained Random Forest model was deployed using Streamlit, providing a user-friendly interface for users to interact with the predictive tool. The deployment is hosted on Streamlit Share and can be accessed [here](https://bankchurners.streamlit.app/)..

## Results

The deployed model achieved an impressive accuracy of 97% in predicting bank customer churn. This high level of accuracy enables financial institutions to effectively identify and address customer churn, ultimately improving profitability and customer satisfaction.

## Conclusion

The Bank Churners Machine Learning project, employing the Random Forest algorithm with a remarkable 97% accuracy, presents a pivotal advancement in the realm of financial analytics. Through meticulous data analysis, feature engineering, and model development, a predictive tool capable of identifying customers at risk of churn with exceptional precision. This achievement not only enhances the operational efficiency of financial institutions but also underscores the potential for data-driven strategies to foster customer retention and drive profitability. Moving forward, the project sets a solid foundation for continuous improvement and innovation, signaling a promising future for leveraging machine learning in the banking sector. 

## Instructions
To use the deployed model, simply visit the deployment link provided above. Enter the necessary parameters and the model will accurately predict if the customer is at risk of churn or not.




