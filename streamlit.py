import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('linear_regression.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🏡 House Price Prediction")
st.write("Enter the house details to predict its price.")

# User input
feature_value = st.number_input("Enter the feature value (e.g., size in sq ft):", min_value=0.0, step=10.0)

if st.button("Predict Price"):
    X_test = np.array([[feature_value]])  # Convert to numpy array
    prediction = model.predict(X_test)[0]
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")
