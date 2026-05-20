| Variable         | Data Type   | Measurement Level   | Description                                                              |
|:-----------------|:------------|:--------------------|:-------------------------------------------------------------------------|
| customerID       | Categorical | Nominal             | Unique identifier for each customer                                      |
| gender           | Categorical | Nominal             | Customer gender (Male/Female)                                            |
| SeniorCitizen    | Categorical | Binary              | Whether the customer is a senior citizen (1/0)                           |
| Partner          | Categorical | Nominal             | Whether the customer has a partner (Yes/No)                              |
| Dependents       | Categorical | Nominal             | Whether the customer has dependents (Yes/No)                             |
| tenure           | Numerical   | Ratio               | Months the customer has stayed with the company                          |
| PhoneService     | Categorical | Nominal             | Whether the customer has phone service (Yes/No)                          |
| MultipleLines    | Categorical | Nominal             | Whether the customer has multiple lines (Yes/No/No phone service)        |
| InternetService  | Categorical | Nominal             | Type of internet service (DSL/Fiber optic/No)                            |
| OnlineSecurity   | Categorical | Nominal             | Whether the customer has online security (Yes/No/No internet service)    |
| OnlineBackup     | Categorical | Nominal             | Whether the customer has online backup (Yes/No/No internet service)      |
| DeviceProtection | Categorical | Nominal             | Whether the customer has device protection (Yes/No/No internet service)  |
| TechSupport      | Categorical | Nominal             | Whether the customer has tech support (Yes/No/No internet service)       |
| StreamingTV      | Categorical | Nominal             | Whether the customer has streaming TV (Yes/No/No internet service)       |
| StreamingMovies  | Categorical | Nominal             | Whether the customer has streaming movies (Yes/No/No internet service)   |
| Contract         | Categorical | Ordinal             | Contract term (Month-to-month/One year/Two year)                         |
| PaperlessBilling | Categorical | Nominal             | Whether the customer uses paperless billing (Yes/No)                     |
| PaymentMethod    | Categorical | Nominal             | Payment method (Electronic check/Mailed check/Bank transfer/Credit card) |
| MonthlyCharges   | Numerical   | Ratio               | Amount charged to the customer monthly                                   |
| TotalCharges     | Numerical   | Ratio               | Total amount charged over the customer's tenure                          |
| Churn            | Categorical | Nominal             | Whether the customer churned (Yes/No)                                    |