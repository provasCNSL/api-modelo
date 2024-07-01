from flask import Flask, request, jsonify

app = Flask(__name__)

import joblib
import numpy as np

# Load the model
model = joblib.load('model.joblib')

# Define the class names
class_names = np.array(['setosa', 'versicolor', 'virginica'])


@app.route('/')
def read_root():
    return {'message': 'Iris model API'}

@app.post('/predict')
def predict():
    data = request.get_json()
    print(data)
    print(data['features'])
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    return {'predicted_class': class_name}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)