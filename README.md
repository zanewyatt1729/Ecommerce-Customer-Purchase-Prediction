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
<<<<<<< HEAD
| HTML/CSS/
=======
| HTML/CSS/JavaScript | Frontend |
| Jupyter Notebook | Model development |
| Joblib | Saving trained models |

## Project Structure

```text
Ecommerce-Customer-Purchase-Prediction/
│
├── app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
│
├── data/
│   └── raw/
│       └── online_shoppers_intention.csv
│
├── models/
│   ├── best_model.joblib
│   ├── preprocessor.joblib
│   └── purchase_prediction_model.joblib
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preprocessing.ipynb
│   └── 03_model_training.ipynb
│
├── reports/
│   ├── figures/
│   └── model_results/
│
├── tests/
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/zanewyatt1729/Ecommerce-Customer-Purchase-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd Ecommerce-Customer-Purchase-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application

```bash
python app/app.py
```

### 7. Open the application

Visit:

http://127.0.0.1:5000

The analytics dashboard is available at:

http://127.0.0.1:5000/dashboard

## Results and Visualizations

The `reports/figures/` directory contains visualizations generated during model development:

- Model comparison
- Confusion matrix
- ROC curve comparison
- Feature importance
- Threshold optimization

## Important Notes and Limitations

- This project predicts purchase intention for an individual browsing session, not long-term customer purchasing behaviour.
- Predictions are based on the features available in the UCI dataset.
- The model provides probabilistic estimates and does not guarantee that a visitor will make a purchase.
- The application stores submitted prediction records, not actual e-commerce transaction data.
- Model performance may vary on real-world data.

## Future Enhancements

- Improve model performance through additional experiments.
- Add user authentication and role-based access.
- Implement CSV export for prediction history.
- Improve dashboard analytics and reporting.
- Deploy the application to a cloud platform.
- Add automated model monitoring and retraining.

## Author

**Sarthak Pandey**

B.Tech – Computer Science and Engineering

GitHub: https://github.com/zanewyatt1729

---

If you find this project interesting, consider giving the repository a star!

