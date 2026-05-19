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
