from fastapi import FastAPI
from data_model import TaxiRide, TaxiRidePrediction # data models imported
from predict import predict

app = FastAPI()

@app.get("/")
def index():
    return {"message": "NYC Taxi Ride Duration Prediction"}


# Post, because Data is being send to the server from the user
@app.post("/predict", response_model=TaxiRidePrediction)
def predict_duration(data: TaxiRide): # Data beeing send in the model of TaxiRide 
    # (RideID, PU, DO, distance)
    prediction = predict("runs:/350d0a6fd4884d47983e1b2b244679f9/model", data) # makes pre-processing and prediction of
    # one instance 
    # In the Return-statement, the input-data of the post-method in the data-model of
    # TaxiRide is unpacked into the data-model of TaxiRidePrediction, which inherits from TaxiRide
    # so that the returned object holds the data about the ride and the predicted duration
    return TaxiRidePrediction(**data.dict(), 
                              predicted_duration=prediction)