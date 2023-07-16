### Predict-script which defines the functions used in the requests of the api
import mlflow
import os
from dotenv import load_dotenv
import numpy as np
from datetime import datetime

### Helper functions
# Time of the day in minutes as feature
def get_days_minutes(time_now):
    '''time_str'''
    return date_time.hour * 60 + date_time.minute

### Functions for the app
# Data Preprocessing for a single ride given as a dict?
def prepare_features(ride):
    ### add the current time in minutes to the ride data
    now_time = datetime.now()
    features = {}

    ### Transform given locatio_ids to a single trip route
    #categorical_features = ["PULocationID", "DOLocationID"]
    features['trip_route'] = str(ride.PULocationID) + "_" + str(ride.DOLocationID)
    features["trip_distance"] = ride.trip_distance
    features["pickup_time_minutes"] = get_days_minutes(now_time)
    features["passenger_count"] = ride.passenger_count

    return features

# Load the Model from ML-Flow
def load_model(model_name):
    stage = "Production"
    model_uri = f"models:/{model_name}/{stage}"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

# Return a prediction
def predict(model_name, data):
  
    load_dotenv()
    MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
    SA_KEY = os.getenv("SA_KEY")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SA_KEY
    
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    model_input = prepare_features(data)
    model = load_model(model_name)
    prediction = model.predict(model_input) # preprocessing pipeline (vectorization and encoding) is part of the pipeline
    return float(prediction[0])             # predicted value

