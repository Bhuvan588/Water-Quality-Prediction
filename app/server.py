from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load("app/model.joblib")

class_names = np.array(["water_not_safe", "water_safe"])

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Water Quality prediction'}


@app.post('/predict')
def predict(data:dict):
    features = np.array(data['features']).reshape(1,-1)
    prediction = model.predict(features)
    class_name = class_names[prediction][0]
    answer ="prediction"
    if(class_name==0):
        answer = "water_not_safe"
    else:
        answer = "water_safe"
    return {'predicted_class': answer}


