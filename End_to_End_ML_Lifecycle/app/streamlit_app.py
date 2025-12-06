import streamlit as st
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np

st.title("📊 Sales Prediction App")

# User Input
st.subheader("🔮 Predict Sales")

quantity = st.number_input("Quantity", 1, 100, 3)
discount = st.number_input("Discount", 0.0, 1.0, 0.0)

# Define options manually
categories = ["Furniture", "Office Supplies", "Technology"]
subcategories = ["Chairs", "Tables", "Phones", "Binders"]
regions = ["East", "West", "Central"]

category = st.selectbox("Category", categories)
subcat = st.selectbox("Sub-Category", subcategories)
region = st.selectbox("Region", regions)

# Prepare Model 
model_file = "sales_model.pkl"

try:
    model, encoder = pickle.load(open(model_file, "rb"))
except:
    st.info("⚡ No model found, creating a temporary demo model...")
    
    # Create dummy training data
    dummy_data = pd.DataFrame({
        "Quantity": np.random.randint(1, 20, 50),
        "Discount": np.random.rand(50),
        "Category": np.random.choice(categories, 50),
        "Sub-Category": np.random.choice(subcategories, 50),
        "Region": np.random.choice(regions, 50),
        "Sales": np.random.randint(100, 1000, 50)
    })

    X = dummy_data[["Quantity", "Discount", "Category", "Sub-Category", "Region"]]
    y = dummy_data["Sales"]

    categorical_cols = ["Category", "Sub-Category", "Region"]
    encoder = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)],
        remainder='passthrough'
    )
    X_encoded = encoder.fit_transform(X)
    model = LinearRegression()
    model.fit(X_encoded, y)

    # Save the model for future use
    pickle.dump((model, encoder), open(model_file, "wb"))

# Predict Button
if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Quantity": quantity,
        "Discount": discount,
        "Category": category,
        "Sub-Category": subcat,
        "Region": region
    }])

    # Encode input
    input_encoded = encoder.transform(input_df)

    # Predict
    prediction = model.predict(input_encoded)[0]
    st.success(f"📈 **Predicted Sales: {prediction:.2f}**")
