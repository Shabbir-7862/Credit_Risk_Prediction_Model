# Credit-Risk-Prediction-Model-Algorithm

    This project builds a machine learning model to predict credit risk using the German Credit Risk Dataset from Kaggle.
    It includes full data preprocessing, model comparison, model serialization, and a simple Streamlit UI for local deployment.

# 🚀 Project Overview

Credit risk prediction is essential for financial institutions to determine whether a borrower is likely to repay a loan.
This project aims to:

    Analyze the German credit dataset

    Perform data cleaning & outlier detection

    Select relevant features

    Train multiple machine learning models

    Select the best-performing algorithm

    Deploy the model using a simple Streamlit interface

# 📂 Dataset

    Name: German Credit Risk Dataset

    Source: Kaggle

    Contains demographic, financial history, and loan–related attributes used to classify applicants as good or bad credit risks.

# 🔍 Steps Followed

1. Exploratory Data Analysis (EDA)

    Loaded the dataset and inspected structure

    Identified outliers using visualization & statistical methods

    Analyzed distribution of key numerical and categorical features

2. Data Preprocessing

    Selected important features and removed irrelevant or noisy columns

    Encoded categorical variables

    Handled outliers appropriately

    Standardized/normalized numerical data (if applicable)

    Saved important transformed objects as .pkl files

3. Train–Test Split

    Separated dataset into training and testing sets

    Used appropriate ratio to ensure balanced distribution

4. Model Training & Comparison

    Trained multiple machine learning models:

    DecisionTreeClassifier

    RandomForestClassifier

    ExtraTreesClassifier

    XGBClassifier

5. Compared models using:

    Accuracy

    Classification report

    Confusion matrix

✅ Best Model: XGBClassifier
This model gave the highest accuracy and consistent performance across validation metrics.

6. Streamlit Application

    Created a simple UI using Streamlit to:

    Load the trained model

    Take user inputs

    Predict credit risk in real time