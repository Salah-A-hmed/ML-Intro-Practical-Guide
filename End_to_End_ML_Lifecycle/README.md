# End to End ML Life Cycle

## 📌 Project Overview

This project is designed as a **complete guide for beginners** to learn and implement the **entire Machine Learning lifecycle** using **real sales data**. It covers everything from **data collection** to **deployment on Streamlit**.

By the end of this project, you will be able to:
- Explore and clean a real sales dataset
- Perform exploratory data analysis (EDA)
- Select and engineer features for your model
- Train a machine learning model to predict sales
- Evaluate model performance
- Save and deploy the model using Streamlit

---

## 📂 Folder Structure

```

End to End ML Life Cycle/
data/
sales_data.csv
notebooks/
EDA_and_Modeling.ipynb
src/
data_processing.py
model_training.py
prediction.py
app/
streamlit_app.py
images/
ml_libraries_1.png
ml_libraries_2.png
requirements.txt
README.md

````

---

## 🛠 ML Lifecycle Steps

### 0. Required Libraries
Here's a quick visual summary of the main Python libraries we need in ML:

![ML Libraries Overview](images/ml_libraries_1.jpg)
![ML Libraries Details](images/ml_libraries_2.jpg)

Main libraries include:
- `pandas` → Data loading & manipulation
- `numpy` → Numerical operations
- `matplotlib` / `seaborn` → Data visualization
- `scikit-learn` → ML models & preprocessing
- `pickle` → Save/load trained models
- `streamlit` → Deployment & interactive apps

---

### 1. Data Collection
- Use a real sales dataset (`sales_data.csv`)
- Example sources: [Kaggle Sample Superstore](https://www.kaggle.com/datasets/), retail sales datasets
- Load dataset using Pandas

### 2. Data Cleaning & EDA
- Check for missing values
- Analyze sales, categories, and regions
- Visualize trends using Matplotlib / Seaborn

### 3. Feature Engineering
- Select important features like `Product Category`, `Price`, `Quantity`, `Region`
- Encode categorical variables if needed

### 4. Model Training
- Split data into training and testing sets
- Train a simple ML model (e.g., Linear Regression, Decision Tree Regressor)
- Evaluate performance using metrics like **MSE** or **R²**

### 5. Model Saving
- Save the trained model using `pickle` for deployment

### 6. Deployment with Streamlit
- Create an interactive Streamlit app (`streamlit_app.py`)
- Users can input product details
- Predict sales using the trained model
- Display results in a friendly interface

---

## 📦 Installation

1. Clone the repository:
```bash
git clone <repo-link>
cd "End to End ML Life Cycle"
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app/streamlit_app.py
```
