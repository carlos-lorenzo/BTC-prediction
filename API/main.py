from fastapi import FastAPI
from makePrediction import predict
#from fastapi.staticfiles import StaticFiles
#from fastapi.templating import Jinja2Templates



app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

#templates = Jinja2Templates(directory="Templates")

modelPrediction = predict()

if modelPrediction[0] == 1:
    prediction = "UP"
    confidence = modelPrediction[1]
    colour = "background-color:#14DCB4"
    
elif modelPrediction[0] == 0:
    prediction = "DOWN"
    confidence = modelPrediction[1]
    colour = "background-color:#DC143C"

else:
    prediction = "NO IDEA XD"
    colour = "background-color:#5014DC"
       
"""
@app.get("/")
def homePage(request:Request):
    return templates.TemplateResponse("homePage.html", {"request": request, 
                                                        "Prediction": prediction,
                                                        "Confidence": confidence,
                                                        "Colour": colour})
"""

@app.get("/")
def homePage():
    return {"Prediction":prediction, "Confidence":confidence}
    