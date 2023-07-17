from pydantic import BaseModel

# For the input data of the user
class TaxiRide(BaseModel):
    ride_id: str
    PULocationID: int
    DOLocationID: int
    trip_distance: float
    passenger_count: int
    

# For the returned data from the server
class TaxiRidePrediction(TaxiRide):
    predicted_duration: float