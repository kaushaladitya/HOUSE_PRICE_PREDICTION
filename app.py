from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open('linear_regression.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Machine Learning Model API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Receive input data as JSON
    X_test = np.array(data['features']).reshape(-1, 1)  # Convert to numpy array
    prediction = model.predict(X_test).tolist()  # Predict
    return jsonify({'prediction': prediction})  # Return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)
