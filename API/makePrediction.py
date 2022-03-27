from scrapeData import get_today
import numpy as np
import pickle

def predict():
    today = get_today()
    with open("btc_model", "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([today])
    confidenceArray = model.predict_proba([today])
    
    downConfidence = np.round(confidenceArray[0], 2) * 100
    upConfidence = np.round(confidenceArray[0], 2) * 100
    if prediction[0] == "0":
        return 0, int(downConfidence[0])
    else:
        return 1, int(upConfidence[1])
        
predict()





