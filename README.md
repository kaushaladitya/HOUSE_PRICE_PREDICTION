# HOUSE_PRICE_PREDICTION
House price prediction using the various machine learning algorithm, done cleaning of the data handle outlier and the apply the hyper tuning method and the many modern machine learning algorithm. 
This project is a Flask-based API for predicting house prices using a trained machine learning model. The model takes various features as input and returns the estimated house price.

# Features
- Supports single and batch predictions
- Uses Flask for API deployment
- Accepts JSON input via POST requests
- Can be integrated with Streamlit for a user-friendly interface

# Tech Stack
- Python
- Flask (Backend API)
- NumPy (Data Handling)
- Scikit-learn (Model Training & Prediction)
- Pickle (Model Serialization)
- Requests (API Testing)

# Installation
- Clone the repository: git clone https://github.com/your-repo/house-price-prediction.git
cd house-price-prediction

- Install dependencies: pip install -r requirements.txt

- Ensure your trained model (linear_regression.pkl) is present in the project directory.


# Running the API
- Start the Flask API server: python app.py


# Streamlit Frontend 
- To create a Streamlit UI for the model:
- Install Streamlit:  pip install streamlit
- Create a streamlit_app.py file and define the UI.
- Run the Streamlit app: streamlit run streamlit_app.py
