from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pipeline
pipeline = joblib.load('customer_segmentation_pipeline.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    new_data = pd.DataFrame([data])

    # Check for unknown categories
    known_categories = ['Female', 'Male']  
    if new_data['Gender'].iloc[0] not in known_categories:
        return jsonify({'error': 'Unknown category in Gender column'}), 400

    # Predict cluster
    cluster = pipeline.predict(new_data)[0]
    return jsonify({'cluster': int(cluster)})

if __name__ == '__main__':
    app.run(debug=True)