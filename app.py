from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Load the model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'random_forest_model.pkl')
model = joblib.load(MODEL_PATH)

# List of feature names in the order expected by the model
FEATURES = ['r', 'i', 'z', 'petroRad_g', 'petroRad_r', 'petroR50_u', 'petroR50_g', 'petroR50_i', 'petroR50_r', 'petroR50_z']

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/input')
def input_page():
	return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
	# Get form data in the correct order
	try:
		values = [float(request.form[feature]) for feature in FEATURES]
	except Exception as e:
		return f"Error in input: {e}", 400
	arr = np.array(values).reshape(1, -1)
	prediction = model.predict(arr)[0]
	# Map prediction to label
	label_map = {1.0: 'Starforming', 0.0: 'Starbursting', 1: 'Starforming', 0: 'Starbursting', '1.0': 'Starforming', '0.0': 'Starbursting'}
	label = label_map.get(prediction, str(prediction))
	session['prediction'] = label
	return redirect(url_for('output'))

@app.route('/output')
def output():
	prediction = session.get('prediction', None)
	if prediction is None:
		return redirect(url_for('input_page'))
	return render_template('output.html', prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)
