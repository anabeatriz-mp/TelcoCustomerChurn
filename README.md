# Telco Customer Churn

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

## 3. Missing Data Analysis

> [!note]
> The Jupyter Notebook that supports the analysis below can be found in [notebooks\missing_data_analysis.ipynb](https://github.com/anabeatriz-mp/TelcoCustomerChurn/blob/master/notebooks/missing_data_analysis.ipynb).

### Missing Values per Variable

A custom `check_missing_values()` function was used to quantify missingness across all columns. The analysis identified a subset of variables carrying missing values, reported both as raw counts and percentages relative to the full dataset. 

The table with the results is the following:

| Variable         | Count of Missing | Percentage |
| -----------      | :--------------: | :--------: | 
| gender           | 750              | 10.65%     |
| Partner          | 1000             | 14.20%     |
| tenure           | 2500             | 35.50%     |
| InternetService  | 1000             | 14.20%     |
| StreamingTV      | 1500             | 21.30%     |
| MonthlyCharges   | 1500             | 21.30%     |
| TotalCharges     | 11               | 0.16%      |

### Missingness Patterns

#### Visual inspection 

A heatmap of `df.isnull()` was plotted to inspect the spatial distribution of missing values. The initial impression was that missingness looked **visually random** — no obvious vertical bands or row clusters. However, this is largely because the dataset's missing data is **synthetically injected**, making it appear randomised by design.

![missing_values_heatmap](https://github.com/anabeatriz-mp/TelcoCustomerChurn/blob/master/reports/plots/missing_values_heatmap.png)

#### NaN Pair Correlation

A pairwise correlation matrix of missingness indicators was plotted, as shown below:

![pairwise nan correlation matrix](https://github.com/anabeatriz-mp/TelcoCustomerChurn/blob/master/reports/plots/nan_pair_correlation_heatmap.png)

It revealed two pairs with **perfect 1.0 correlation**:

- `InternetService` ↔ `Partner`
- `StreamingTV` ↔ `MonthlyCharges`

A correlation of 1.0 means these variables are **missing in the exact same rows** — no exceptions. This strongly supports the hypothesis that missing data was injected in **blocks** (i.e., multiple columns deleted from the same rows simultaneously), rather than independently per column.
 
Most other inter-column missingness correlations are also notably high, suggesting widespread row-level co-occurrence of missing values.

#### Structural missingness of `TotalCharges`

`TotalCharges` was flagged as a special case, as the pairwise missing correlation heatmap showed no relation to any of the other features. 

The `check_structural_missingness()` function revealed that **all missing values in `TotalCharges` correspond to a single unique value in `tenure`** — strongly suggesting that customers with `tenure = 0` (i.e., brand new customers) simply have no charges to report yet. This is a textbook case of **structural missingness** where the value isn't missing at random, it's absent *by design*.

### Possible Interpretations and Mechanisms

The table below shows, for each column in the dataset, the suspected missing mechanism and the interpretation behind it.

|     Variable    | Suspected Mechanism |                                  Interpretation                                  |
|:---------------:|:-------------------:|:--------------------------------------------------------------------------------:|
| gender          |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |
| Partner         |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |
| tenure          |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |
| InternetService |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |
| StreamingTV     |      Structural     | New customers (tenure = 0) have no accumulated charges; NaN semantically means 0 |
| MonthlyCharges  |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |
| TotalCharges    |   MCAR (synthetic)  | High inter-column missingness correlation points to row-level block injection    |


**On mechanisms:**

- **MCAR** (Missing Completely At Random) is the most defensible hypothesis for the majority of variables, given the synthetic origin of the dataset. The missingness does not appear to relate to the actual values of those variables or any other observed variable - it was externally injected.
- **MNAR** (Missing Not At Random) applies specifically to `TotalCharges`, where the missingness *is* determined by an observed variable (`tenure`), but the relationship is structural rather than probabilistic.
- **MAR** (Missing At Random) could technically apply if the block-injection was conditioned on some other variable, but there's no evidence of that here.

### Variables Where Missingness Has Semantic Meaning

**`TotalCharges`** is the only variable where missingness carries a clear semantic interpretation: `NaN` = customer has not yet been charged (tenure = 0).
 
The co-missing pairs (`InternetService`/`Partner`, `StreamingTV`/`MonthlyCharges`) do **not** have an obvious domain-level reason to be jointly absent, reinforcing that their co-missingness is an artefact of synthetic data construction rather than a real-world phenomenon.

### Possible Imputation Strategies

#### `TotalCharges` → **Domain-based imputation**
 
Since missingness is structural and the underlying formula to obtain `TotalCharges` is known:
 
$$\text{TotalCharges} = \text{tenure} \times \text{MonthlyCharges}$$
 
Missing values will be imputed using this formula so that no information is lost.

#### All other columns with missing values → **Evaluate before imputing**

Given that ~35.6% of rows carry at least one missing value, **row removal is ruled out** — the data loss would be too severe.

To decide if imputation is a good choice, a per-column analysis of value distributions was carried out:
- **Categorical columns**: checked via `value_counts(normalize=True)` to ensure imputation doesn't distort class balance.
- **Numerical columns**: inspected via `.describe()` to assess whether mean/median imputation would introduce significant distributional distortion.


**Imputation strategy** (justified by MCAR assumption):
- **Categorical variables**: mode imputation or a dedicated `"Unknown"` category, depending on whether the missingness proportion is large enough to warrant its own label, or if it makes sense given the variables descriptions.
- **Numerical variables**: median imputation (more robust to skew than mean).

## 4. Univariate Analysis

The dataset contains **3 numerical** and **17 categorical** variables. Analysis was conducted separately for each type.

### Numerical  Variables

Descriptive statistics were computed including mean, median, Standard Deviation, Coefficient of Variation (CV), quartiles, Interquartile Range (IQR), Skewness, and Kurtosis.

#### Summary Table

| Feature        |   Count |      Mean |   Median |   Std Dev |       CV |   Min |     Q1 |       Q3 |      IQR |    Max |   Skewness |   Kurtosis |
|:---------------|--------:|----------:|---------:|----------:|---------:|------:|-------:|---------:|---------:|-------:|-----------:|-----------:|
| `tenure`         |    4543 |   32.5466 |    29    |   24.5055 | 0.752937 |  0    |   9    |   56     |   47     |   72   |   0.231347 |  -1.38799  |
| `MonthlyCharges` |    5543 |   64.8764 |    70.55 |   30.1013 | 0.46398  | 18.25 |  35.75 |   89.925 |   54.175 |  118.6 |  -0.227777 |  -1.26222  |
| `TotalCharges`   |    7032 | 2283.3    |  1397.47 | 2266.77   | 0.992761 | 18.8  | 401.45 | 3794.74  | 3393.29  | 8684.8 |   0.961642 |  -0.231799 |

> Note: differing Count values reflect the missing data addressed in section 3.

#### Distribution Plots

Histograms with KDE overlays and boxplots were generated for all three variables, as shown below:

![plot of numerical variables distributions](https://github.com/anabeatriz-mp/TelcoCustomerChurn/blob/master/reports/plots/plot_numerical_distributions_univariate.png)

**Key Observations**
- **tenure**: Values spread across its full range (0–72 months), with a near-uniform shape. The negative kurtosis (−1.39) confirms flat, platykurtic tails, no extreme outliers.
- **MonthlyCharges**: Roughly bimodal. Light negative skew; also platykurtic.
- **TotalCharges**: Right-skewed (0.96), which is expected — it's the product of tenure and monthly charges, so long-tenured customers accumulate disproportionately large totals. Wide IQR (3,393) signals high spread.

#### Quality Table

A quality table was computed using thresholds on CV, skewness, and kurtosis:

| Variable         | Challenges                                         |
| -----------      | :-------------------------------------------------:| 
| `tenure`           | High Variability (CV = 0.75)                     |
| `MonthlyCharges`   | Statistically well-behaved                       |
| `TotalCharges`     | High Variability (CV = 0.99), Moderately Skewed  |

**Conclusions:**

- **tenure**: High CV reflects a wide range of customer lifetimes, from brand new (0) to loyal (72 months). Might benefit from binning into lifecycle stages (e.g., new / mid / loyal) for certain models.
- **TotalCharges**: The combination of high variability and moderate right skew makes this a statistically challenging numeric variable. A log transformation would compress the long tail and bring the distribution closer to symmetry.
- **MonthlyCharges**: The most well-behaved of the three, though the bimodal shape may warrant investigation in later bivariate analysis (it likely tracks with contract type or internet service tier).

### Categorical Variables


#### Summary Table

| Feature          |   Cardinality | Cardinality Level   | Biggest Category   | % of Biggest Category   |   Num Rare Levels | Missing %   |
|:-----------------|--------------:|:--------------------|:-------------------|:------------------------|------------------:|:------------|
| gender           |             2 | Low                 | Male               | 50.88 %                 |                 0 | 10.65 %     |
| SeniorCitizen    |             2 | Low                 | No                 | 83.79 %                 |                 0 | 0.00 %      |
| Partner          |             2 | Low                 | No                 | 51.55 %                 |                 0 | 14.20 %     |
| Dependents       |             2 | Low                 | No                 | 70.04 %                 |                 0 | 0.00 %      |
| PhoneService     |             2 | Low                 | Yes                | 90.32 %                 |                 0 | 0.00 %      |
| MultipleLines    |             3 | Low                 | No                 | 48.13 %                 |                 0 | 0.00 %      |
| InternetService  |             3 | Low                 | Fiber optic        | 44.02 %                 |                 0 | 14.20 %     |
| OnlineSecurity   |             3 | Low                 | No                 | 49.67 %                 |                 0 | 0.00 %      |
| OnlineBackup     |             3 | Low                 | No                 | 43.84 %                 |                 0 | 0.00 %      |
| DeviceProtection |             3 | Low                 | No                 | 43.94 %                 |                 0 | 0.00 %      |
| TechSupport      |             3 | Low                 | No                 | 49.31 %                 |                 0 | 0.00 %      |
| StreamingTV      |             3 | Low                 | No                 | 39.67 %                 |                 0 | 21.30 %     |
| StreamingMovies  |             3 | Low                 | No                 | 39.54 %                 |                 0 | 0.00 %      |
| Contract         |             3 | Low                 | Month-to-month     | 55.02 %                 |                 0 | 0.00 %      |
| PaperlessBilling |             2 | Low                 | Yes                | 59.22 %                 |                 0 | 0.00 %      |
| PaymentMethod    |             4 | Low                 | Electronic check   | 33.58 %                 |                 0 | 0.00 %      |
| Churn            |             2 | Low                 | No                 | 73.46 %                 |                 0 | 0.00 %      |


#### Cardinality

All variables fall into the Low cardinality category (< 10 unique values). No high-cardinality variables are present, so no cardinality reduction or hashing strategies are needed.

#### Frequency Distributions and Class Balance

Most binary variables are reasonably balanced, with a few exceptions:
- **SeniorCitizen**: Strongly skewed — 83.8% of customers are non-seniors.
- **PhoneService**: 90.3% of customers have phone service (nearly a constant).
- **Churn**: 73.5% of customers did not churn. Class imbalance is moderate and should be addressed during modelling.

#### Rare Levels

No rare levels were found across any categorical variable. Every category in every column meets the ≥ 5% frequency threshold, so no collapsing or grouping of levels is necessary.















