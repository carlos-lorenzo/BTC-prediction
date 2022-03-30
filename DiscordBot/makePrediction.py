from scrapeBTC_h1 import returnFeatures
from scrapeBTC_D import get_today
import numpy as np
import pickle

def predict_h1():
    features = returnFeatures()
    
    with open("btc_model_h1", "rb") as f:
        model = pickle.load(f)
        
    prediction = model.predict([features])
    confidenceArray = model.predict_proba([features])
    
    downConfidence = np.round(confidenceArray[0], 2) * 100
    upConfidence = np.round(confidenceArray[0], 2) * 100
    
    if prediction[0] == "0":
        return "Going Down", int(downConfidence[0])
    else:
        return "Going Up", int(upConfidence[1])
    
    
def predict_D():
    features = get_today()
    
    with open("btc_model_D", "rb") as f:
        model = pickle.load(f)
        
    prediction = model.predict([features])
    confidenceArray = model.predict_proba([features])
    
    downConfidence = np.round(confidenceArray[0], 2) * 100
    upConfidence = np.round(confidenceArray[0], 2) * 100
    
    if prediction[0] == "0":
        return "Going Down", int(downConfidence[0])
    else:
        return "Going Up", int(upConfidence[1])
    
        


