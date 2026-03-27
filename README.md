# 🏠 House Price Prediction API (Multiple Linear Regression)

This project implements a **house price prediction system** using **Multiple Linear Regression** on the Boston Housing dataset.  
It includes **data analysis, model training, evaluation, and deployment via FastAPI**.

---

## 📌 1. Dataset Selection

For this project, the **Boston Housing dataset** was used:

🔗 https://www.geeksforgeeks.org/machine-learning/boston-dataset-in-sklearn/

### Why this dataset?

- Contains real-world housing data
- Suitable for regression tasks
- Includes multiple independent variables → perfect for **Multiple Linear Regression**
- Widely used for educational and benchmarking purposes

---

## 📊 2. Dataset Overview

The Boston Housing dataset is a **prebuilt dataset in sklearn** used for regression tasks.

### General Information:

- **Total samples:** 506  
- **Number of features:** 13  
- **Feature type:** Real, positive values  
- **Target (`medv`):** Real values in range ~5 to 50 (in $1000s)

---

## 📖 Feature Description

The dataset contains several features describing different aspects of residential areas:

| Feature | Description |
|--------|------------|
| `CRIM` | Per capita crime rate by town |
| `ZN` | Proportion of residential land zoned for large lots |
| `INDUS` | Proportion of non-retail business acres |
| `CHAS` | Near Charles River (1 = yes, 0 = no) |
| `NOX` | Nitric oxide pollution level |
| `RM` | Average number of rooms per dwelling |
| `AGE` | Proportion of houses built before 1940 |
| `DIS` | Distance to employment centers |
| `RAD` | Accessibility to highways |
| `TAX` | Property tax rate per $10,000 |
| `PTRATIO` | Pupil-teacher ratio |
| `BLACK` | Proportion of Black population (historical variable in dataset) |
| `LSTAT` | % lower status population |
| `MEDV` | Median house value (**target**) |

---

## 🧠 Interpretation

- Higher `RM` → usually **higher house price**
- Higher `TAX` → often **lower house price**
- Higher `CRIM` → usually **negative impact**
- `CHAS = 1` → often slightly **higher value** (river proximity)

---

## ⚠️ Notes

- Some features (e.g., `CRIM`, `NOX`, `LSTAT`) are harder for users to input manually.
- Therefore, only a subset of features was used in the final model to improve usability.

## 🧹 3. Data Preprocessing

### Steps performed:

1. Loaded dataset using `pandas`
2. Checked for missing values → none found
3. Dropped unnecessary columns:

```python
["Unnamed: 0", "indus", "crim", "nox", "dis", "ptratio", "lstat", "rad", "black"]
````

### Why were these removed?

* Hard for users to input manually
* Not essential for a simple prediction interface
* Improves usability of the API

---

## 🎯 4. Feature Selection

Final selected features:

```python
zn, chas, rm, age, tax
```

### Reason:

* Easy for users to understand and input
* Still provide reasonable predictive power
* Balance between **accuracy** and **usability**

---

## 📈 5. OLS Regression (Statistical Analysis)

Before training the model, **OLS (Ordinary Least Squares)** was used:

```python
X_sm = sm.add_constant(X)
ols_model = sm.OLS(y, X_sm).fit()
```

### Purpose:

* Analyze feature importance
* Check p-values
* Understand relationships between variables

---

## 🔀 6. Train/Test Split

```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

* 80% → training
* 20% → testing
* `random_state=42` ensures reproducibility

---

## 🤖 7. Model Training

Model used:

```python
LinearRegression()
```

### Why Linear Regression?

* Simple and interpretable
* Suitable for multiple input variables
* Meets requirement: **Multiple Linear Regression**

---

## 📊 8. Model Evaluation

Metrics used:

* **R² (coefficient of determination)** → model accuracy
* **MAE (Mean Absolute Error)** → average error
* **MSE (Mean Squared Error)** → penalizes large errors
* **RMSE (Root Mean Squared Error)** → interpretable error

Example output:

```
R²: 0.6715
MAE: 3.1497
MSE: 24.0884
RMSE: 4.908
```

---

## 💾 9. Model Saving

The trained model is saved using `pickle`:

```python
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## ⚙️ 10. Backend (FastAPI)

A REST API was built using **FastAPI**.

### Endpoints:

#### 1. Predict using JSON body

```
POST /house/predict
```

Input:

```json
{
  "zn": 18,
  "chas": 0,
  "rm": 6.5,
  "age": 65,
  "tax": 300
}
```

---

#### 2. Predict using query parameters

```
POST /house/predict/params?zn=18&chas=0&rm=6.5&age=65&tax=300
```

---

## 🔄 11. Input Preprocessing

Input is converted into a DataFrame:

```python
data = {
    "zn": house.zn,
    "chas": house.chas,
    "rm": house.rm,
    "age": house.age,
    "tax": house.tax,
}
```

---

## ⚠️ 12. Handling Invalid Predictions

Linear regression can sometimes produce **negative values**, which are unrealistic.

### Solution:

```python
if prediction < 0:
    raise ExpectationFailed417
```

### Why?

* A house price cannot be negative
* Prevents invalid outputs
* Improves API reliability

---

## 🔢 13. Output Formatting

* Rounded to **1 decimal place**
* Returned as:

```json
{
  "medv": 4.5
}
```

---

## 📁 14. Project Structure

```
backend/
 └── src/
      └── house/
           ├── service.py
           ├── schema.py
           └── endpoint.py
           └── static/
                ├── model.pkl
                └── Boston.csv
```

---

## 📊 Model Evaluation & Trade-off

### Full Feature Model

When using **all available features**, the model achieved:

- **R²:** 0.6688  
- **MAE:** 3.1891  
- **MSE:** 24.2911  
- **RMSE:** 4.9286  

### Reduced Feature Model (Final Version)

After removing complex features and keeping only user-friendly inputs:

- **R²:** ~0.49  

---

## ⚖️ Explanation of the Difference

The drop in performance is expected and intentional.

### Why did performance decrease?

- The model originally used **13 features**
- Many of them contain important information:
  - `lstat` → strong indicator of socioeconomic status  
  - `crim` → crime rate  
  - `nox` → pollution  
- Removing them reduces the amount of information available to the model

👉 Less information = lower prediction accuracy

---

## 🎯 Why reduce features anyway?

The goal of this project is not only accuracy, but also **usability**.

### Problems with full-feature model:

- Users cannot realistically input:
  - pollution levels (`nox`)
  - crime rates (`crim`)
  - socioeconomic indicators (`lstat`)
- Makes the API impractical

---

## ✅ Final Decision

We chose a **simplified model** using:

```python
zn, chas, rm, age, tax
```
