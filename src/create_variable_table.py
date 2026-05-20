import pandas as pd
import os

data_dict = [
    {"Variable": "customerID",       "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Unique identifier for each customer"},
    {"Variable": "gender",           "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Customer gender (Male/Female)"},
    {"Variable": "SeniorCitizen",    "Data Type": "Categorical", "Measurement Level": "Binary",  "Description": "Whether the customer is a senior citizen (1/0)"},
    {"Variable": "Partner",          "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has a partner (Yes/No)"},
    {"Variable": "Dependents",       "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has dependents (Yes/No)"},
    {"Variable": "tenure",           "Data Type": "Numerical",   "Measurement Level": "Ratio",   "Description": "Months the customer has stayed with the company"},
    {"Variable": "PhoneService",     "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has phone service (Yes/No)"},
    {"Variable": "MultipleLines",    "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has multiple lines (Yes/No/No phone service)"},
    {"Variable": "InternetService",  "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Type of internet service (DSL/Fiber optic/No)"},
    {"Variable": "OnlineSecurity",   "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has online security (Yes/No/No internet service)"},
    {"Variable": "OnlineBackup",     "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has online backup (Yes/No/No internet service)"},
    {"Variable": "DeviceProtection", "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has device protection (Yes/No/No internet service)"},
    {"Variable": "TechSupport",      "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has tech support (Yes/No/No internet service)"},
    {"Variable": "StreamingTV",      "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has streaming TV (Yes/No/No internet service)"},
    {"Variable": "StreamingMovies",  "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer has streaming movies (Yes/No/No internet service)"},
    {"Variable": "Contract",         "Data Type": "Categorical", "Measurement Level": "Ordinal", "Description": "Contract term (Month-to-month/One year/Two year)"},
    {"Variable": "PaperlessBilling", "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer uses paperless billing (Yes/No)"},
    {"Variable": "PaymentMethod",    "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Payment method (Electronic check/Mailed check/Bank transfer/Credit card)"},
    {"Variable": "MonthlyCharges",   "Data Type": "Numerical",   "Measurement Level": "Ratio",   "Description": "Amount charged to the customer monthly"},
    {"Variable": "TotalCharges",     "Data Type": "Numerical",   "Measurement Level": "Ratio",   "Description": "Total amount charged over the customer's tenure"},
    {"Variable": "Churn",            "Data Type": "Categorical", "Measurement Level": "Nominal", "Description": "Whether the customer churned (Yes/No)"},
]

output_path = os.path.join(os.path.dirname(__file__), "..", "reports", "variable_table.md")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

pd.DataFrame(data_dict).to_markdown(output_path, index=False)