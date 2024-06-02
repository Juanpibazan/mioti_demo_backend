import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import sklearn

rf_model = pickle.load(open('rf2_model.pkl','rb'))

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'Bienvenido a Movie Advisor!!'}


class Characteristics(BaseModel):
        title: str
        startYear: int
        genre: str
        minutes: int
        personType: str
        personName: str
        personAge: float

@app.post('/')
async def predict(characteristics: Characteristics):
    
    return characteristics
