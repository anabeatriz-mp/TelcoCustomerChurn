# Telco Customer Churn
---

## 1. Dataset Description


### Source and Origin

The dataset used in this project is the [**Telco Customer Churn dataset**](https://www.kaggle.com/datasets/jethwaaatmik/telco-customer-churn-dataset), originally published as part of IBM's sample data collections and widely distributed through Kaggle from where I've taken the .csv file.

Its stated purpose is to support the development of customer retention strategies by enabling analysis and prediction of churn behavior in a fictional telecommunications company.


### Units of Analysis

The unit of analysis is the **individual customer**.

The dataset has **7,043 rows** (customers) and **21 columns** (features), with the target variable being Churn — a binary indicator of whether a customer left the service. The remaining 20 variables cover three broad domains:
- **Demographic information about customers** – gender, age range, and if they have partners and dependents.
- **Subscribed services** - phone lines, internet type, online security, backup, device protection, tech support, and streaming services.
- **Customer account information** – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.

### Description of Target Variable

The target variable, `Churn`, is a `binary` flag (Yes/No) capturing whether a customer had discontinued the service at the time of data collection. 

The observed churn rate is approximately 26%, indicating a moderately imbalanced classification problem. This variable supports supervised learning tasks as well as descriptive analysis of churn drivers.


### Claims the Dataset Supports

In terms of what claims the data can support, it is well-suited for:
- **Predictive Claims** - you can build classification models that can predict customers that are more likely to leaving.
- **Correlational Demographics** - you can claim statistical associations between specific attributes and attrition, for example, seeing if customers who are in specific types of contracts are more likely to churn.
- **Service Vulnerabilities** - you can verify if there's higher rates of churn among some services who do not subscribe to add-ons.


### Limitations

This dataset has a few known limitations such as:
1. The dataset originates from a **synthetic IBM sample**, not a real telecom operator which means findings cannot be generalized to actual industry populations
2. **The class imbalance** (~74% non-churn vs. ~26% churn) may bias model performance toward the majority class if not addressed

---


## 2. Variable Dictionary and Measurement Types



### Variable Table

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


### Discussion
The majority of variables in this dataset are nominal — they represent unordered categories where only equality or difference can be meaningfully assessed. Variables like `gender`, `PaymentMethod`, or `InternetService` carry no inherent rank; no category is "greater than" another.

`Contract` is the only variable classified as ordinal. Month-to-month, one-year, and two-year contracts imply a natural progression in commitment level and, plausibly, in switching costs and customer stability. Treating it as nominal would discard that structure entirely; treating it as numeric would impose equal spacing between levels that may not hold in practice.

The three continuous variables — `tenure`, `MonthlyCharges`, and `TotalCharges` — are ratio-scale, meaning they have a true zero and support arithmetic operations.

### Variables with Ambiguous Interpretations

Variables like `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, and `StreamingMovies` contain the category "No internet service". Similarly, `MultipleLines` contains "No phone service". This is ambiguous because it blends a service status with a feature status. It also creates massive multicollinearity; if `InternetService` = "No", then all six of those dependent columns will redundantly say "No internet service".

The `SeniorCitizen` threshold is coded simply as 1 or 0. The metadata does not define the age threshold (e.g., 65+). Furthermore, it is the only binary variable coded numerically rather than as "Yes/No", creating an inconsistency in the data's raw formatting.

### Variables That May Require Transformation or Recoding

To prepare this data for exploratory data analysis (EDA) and predictive modeling (like Churn prediction), the following transformations may be needed:

#### Cleaning & Standardization

- Drop `customerID`: Remove this column before training any model to prevent the algorithm from memorizing identifiers (overfitting).
- Convert `SeniorCitizen` from `1 / 0` to `Yes / No` (or map all Yes/No variables to 1/0) so all binary columns follow a unified convention.
- Fix the `TotalCharges` column to a numeric data type, coercing any blank spaces to NaN, and then impute those missing values.

#### Encoding

- Convert "No internet service" and "No phone service" in the sub-feature columns to simply "No". The lack of internet is already captured by the `InternetService` column, so changing these to standard binary (Yes/No) features eliminates redundant noise.
- The variable `Contract` if encoded to ordinal integers (0,1,2) preserves the rank but imposes equal spacing, while one-hot-encoding treats them as fully independent. This decision needs further analysis depending on how the model behaves.

### Why Variable Type is an Analytical Decision and not just Metadata

Relying solely on metadata to assign variable types risks losing contextual information that is critical when building predictive models. What a dataset reports as numeric is not necessarily interval or ratio in meaning — and what appears categorical may carry ordinal structure worth preserving. Defaulting to software-assigned types without scrutiny can lead to models that misrepresent the data's underlying structure.

The research objective also shapes these choices. `tenure`, for instance, could be treated as continuous in a regression, or discretized into lifecycle cohorts if the goal is customer segmentation. Neither is inherently correct — the right encoding depends on what structure is analytically relevant.

Every decision about variable type should therefore reflect an understanding of **the context and structure** that analysis requires, not simply what the raw data **provides**.


