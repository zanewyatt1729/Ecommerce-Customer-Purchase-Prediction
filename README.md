# E-Commerce Customer Purchase Prediction

A Machine Learning-based web application that predicts whether an online shopping session is likely to result in a purchase.

Built using Python, Scikit-learn, Flask, SQLite and data visualization tools.

## Project Overview

E-commerce businesses receive thousands of website visits, but not every visitor makes a purchase. Understanding which browsing sessions are more likely to convert can help businesses improve their marketing strategies and customer experience.

This project uses machine learning to analyze online shopping session data and predict purchase intention.

Users can enter browsing-session information into a web interface and receive a purchase prediction with a probability score. The application also maintains prediction history and provides an analytics dashboard.

## Features

- Exploratory Data Analysis (EDA)
- Data preprocessing and feature engineering
- Machine Learning model training and comparison
- Hyperparameter tuning
- Purchase probability prediction
- Flask-based web application
- SQLite prediction history
- Analytics dashboard with visualizations
- Saved machine learning model for inference

## Machine Learning Models

The following algorithms were implemented and evaluated:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

RandomizedSearchCV was used for hyperparameter tuning of the Decision Tree and Random Forest models.

## Model Performance

The final Random Forest model was evaluated using a separate test dataset.

| Metric | Result |
|---|---:|
| Accuracy | 77.25% |
| Precision | 33.82% |
| Recall | 48.95% |
| F1-Score | 40.00% |
| ROC-AUC | 76.29% |

The classification threshold was optimized using a validation subset, with a selected threshold of 0.55.

The model achieved a recall of 48.95%, identifying 187 out of 382 actual purchase sessions in the test set.

**Note:** The dataset is imbalanced, so accuracy alone is not sufficient to evaluate the model. Precision, recall, F1-score and ROC-AUC are also considered.

## Dataset

**Online Shoppers Purchasing Intention Dataset**

Source: UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

Dataset information:
- 12,330 browsing sessions
- 18 columns
- 17 input features and one target variable
- Target variable: `Revenue`
- No missing values in the original dataset

The dataset contains information about visitor browsing behaviour, page interactions, session duration, visitor type, month and other session characteristics.

Dataset attribution: UCI Machine Learning Repository, Online Shoppers Purchasing Intention Dataset. Licensed under CC BY 4.0.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| Flask | Web application |
| SQLite | Prediction history storage |
| HTML/CSS/
