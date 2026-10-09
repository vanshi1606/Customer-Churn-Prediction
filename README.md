# Customer Churn Prediction | Machine Learning

**An Interactive Machine Learning Dashboard for Customer Retention Analysis**

[ Live Demo](https://vanshi-churn-prediction.streamlit.app/) | [💻 GitHub Repository](https://github.com/vanshi1606/Customer-Churn-Prediction)

## Project Overview

Customer churn refers to customers discontinuing their relationship with a company or service provider. Predicting churn helps businesses identify customers who may leave and plan effective retention strategies.

This project uses a trained machine learning classification model and an interactive Streamlit dashboard to estimate the likelihood of customer churn.

The dashboard allows users to enter customer information, view prediction probabilities, understand customer risk levels, and explore suggested retention actions.

##  Key Features

- **Customer Churn Prediction:** Predicts whether a customer is likely to churn or stay.
- **Interactive Input Controls:** Adjust tenure, monthly charges, total charges, contract type, internet service, and technical support.
- **Churn Probability:** Displays the model's estimated churn probability.
- **Risk Classification:** Categorizes customers into low, medium, and high-risk groups.
- **Interactive Dashboard:** Presents prediction results and customer inputs through visualizations.
- **Business Recommendations:** Suggests customer retention actions based on the predicted risk.

##  Dashboard Visualizations

The dashboard includes:

1. **Churn vs Stay Chart** — Compares predicted churn and retention probabilities.
2. **Risk Meter** — Displays the estimated churn probability visually.
3. **Customer Profile Chart** — Shows selected customer characteristics.
4. **Probability Distribution** — Visualizes churn versus stay probabilities.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Machine learning classification |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Streamlit | Interactive web application |
| Jupyter Notebook | Model development and experimentation |
| GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Web application deployment |

##  Project Structure

```text
Customer-Churn-Prediction/
├── churnapp.py
├── churn_model.pkl
├── project churn.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

##  Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/vanshi1606/Customer-Churn-Prediction.git
```

**2. Navigate to the project folder**

```bash
cd Customer-Churn-Prediction
```

**3. Install required dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run churnapp.py
```

The application should open in your browser.

##  Prediction Workflow

1. Enter the customer's tenure and billing details.
2. Select the customer's contract and service information.
3. Click **Predict Churn**.
4. Review the prediction and estimated churn probability.
5. Examine the risk classification and suggested retention strategies.

### Risk Categories

| Risk Level | Predicted Churn Probability |
|---|---|
| 🟢 Low | 0%–40% |
| 🟡 Medium | Above 40% up to 70% |
| 🔴 High | Above 70% |

These are application-defined thresholds, not guarantees about actual customer behavior.

##  Business Applications

- Identify customers who may be at risk of leaving.
- Support customer retention planning.
- Prioritize customers for follow-up.
- Demonstrate how machine learning can support business decisions.

##  Live Application

Try the deployed dashboard:

**[Launch Customer Churn Prediction Dashboard](https://vanshi-churn-prediction.streamlit.app/)**

##  Future Enhancements

- Downloadable customer prediction reports
- Model performance and evaluation dashboard
- Batch prediction using CSV upload
- Advanced customer segmentation
- Model explainability and feature importance
- Improved responsive charts and dashboard design

## Disclaimer

Predictions are model-generated estimates. Results should be validated against real-world data and should not be treated as guaranteed customer outcomes.

---

**Developed as a Machine Learning and Data Science project.**
