import pandas as pd

df = pd.read_csv("data/raw/telco_data.csv")

def clean_data(df) -> pd.DataFrame:

    """
    Cleans the Telco Customer Churn dataset by performing the following operations:
        1. Drops the 'customerID' as it is not useful for modeling and can lead to overfitting.
        2. Converts the 'SeniorCitizen' column from 1/0 to Yes/No.
        3. Converts the 'TotalCharges' column to a numeric data type, coercing any blank spaces to NaN.

    Returns:
        A cleaned DataFrame ready for analysis and modeling.
    """

    df = df.drop(columns=["customerID"])
    
    df["SeniorCitizen"] = df["SeniorCitizen"].map({1: "Yes", 0: "No"})
    
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    return df


df = clean_data(df)
df.to_csv("data/processed/processed_telco_customer_churn.csv", index=False)
