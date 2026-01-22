# Lung Cancer Classification using K-Nearest Neighbors (Snowflake Data)

This project implements a **K-Nearest Neighbors (KNN)** classifier to
predict lung cancer outcomes using data retrieved from a **Snowflake
data warehouse**. The workflow demonstrates data extraction, categorical
encoding, model training, and evaluation using Python and scikit-learn.

---

## Overview

The objective of this project is to classify whether a patient has lung
cancer (`LUNG_CANCER`) based on demographic and clinical attributes.
The data is sourced directly from Snowflake, making this a combined
**data engineering and machine learning** project.

---

## Data Source
- Platform: Snowflake
- Database: User-defined database
- Schema: User-defined schema
- Table: `CANCER`
- Target column: `LUNG_CANCER`

**Security Note**  
Snowflake credentials should **never** be hardcoded in public
repositories. Use environment variables or secure configuration methods
for real-world applications.

---

## Workflow

### 1. Data Extraction
- Connected to Snowflake using `snowflake-connector-python`
- Executed a SQL query to fetch data from the `CANCER` table
- Loaded query results into a pandas DataFrame
- Closed the Snowflake connection after data retrieval

---

### 2. Data Exploration
- Displayed sample records from the dataset
- Inspected unique values in each column to understand data distribution

---

### 3. Data Preprocessing
- Applied **Label Encoding** to categorical features
- Skipped encoding for the numerical column (`AGE`)
- Converted all non-numeric attributes into numeric form suitable for
  machine learning models

---

### 4. Feature and Target Separation
- Features (`X`): All columns except `LUNG_CANCER`
- Target (`y`): `LUNG_CANCER`

---

### 5. Train–Test Split
- Split the dataset into training and testing sets
- 70% training, 30% testing
- Fixed random state for reproducibility

---

### 6. Model Training
- Algorithm: **K-Nearest Neighbors (KNN)**
- Number of neighbors (`k`) set to 3
- Trained the model on the training dataset

---

### 7. Model Evaluation
- Predicted lung cancer outcomes on the test set
- Evaluated model performance using **accuracy score**

---

## Libraries Used
- pandas
- scikit-learn
- snowflake-connector-python

---

## How to Run

### 1. Install Dependencies
```bash
pip install pandas scikit-learn snowflake-connector-python
