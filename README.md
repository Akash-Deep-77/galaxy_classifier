# Galaxy Classification using Machine Learning

This project is a Flask-based web application that predicts the type of galaxy (Starforming or Starbursting) using a pre-trained Random Forest model. Users can input 10 galaxy features, and the app will display the predicted class along with a representative image.

## Features
- Simple web interface with three pages: Home, Input, and Output
- Predicts galaxy type using a machine learning model (`random_forest_model.pkl`)
- Displays a relevant image for each prediction
- Modern, responsive UI with custom styling

## Folder Structure
```
galaxy_classifier/
│
├── app.py
├── requirements.txt
├── random_forest_model.pkl     (Download from here: https://1drv.ms/u/c/67d012aebe58245d/ET8o0Ae9JpFHvr-DuFi-Q_ABbnZhlvFFsrQM0s4TOmQS9Q?e=cyG94S)     
├── Static/
│   ├── 1.avif
│   ├── 2.jpg
│   ├── sb.webp
│   ├── sf.jpg
│   └── style.css
├── Templates/
│   ├── home.html
│   ├── input.html
│   └── output.html
└── Training Data/
    └── sdss.ipynb
```

## Setup Instructions

### 1. Clone or Download the Repository
```
git clone <repo-url>
cd galaxy_classifier
```

### 2. Create and Activate a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate # On Mac/Linux
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Application
```
python app.py
```

The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
1. Go to the Home page.
2. Click "Start Prediction" to go to the input form.
3. Enter the 10 required galaxy features.
4. Submit the form to see the predicted galaxy type and a relevant image.

## Remote Deployment
- You can deploy this app to any cloud platform that supports Python and Flask (e.g., Heroku, PythonAnywhere, Azure, AWS Elastic Beanstalk).
- Make sure to set up environment variables and install all dependencies as per `requirements.txt`.
- For production, set `debug=False` in `app.py`.

## Requirements
- Python 3.8+
- See `requirements.txt` for all Python dependencies

## Notes
- The model file (`random_forest_model.pkl`) must be present in the project root.
- All static files (images, CSS) should be in the `Static/` folder.
- All HTML templates should be in the `Templates/` folder."# galaxy_classification" 
