from fastapi import FastAPI
from pydantic import BaseModel
import RiddlesPy



riddles = RiddlesPy.Riddle()
app = FastAPI()


class Riddle(BaseModel):
  id: int
  description: str
  question: str
  response: str


@app.get('/')
def index():
  return {'message': "Api direcionado para manipulação de enigmas."}


@app.get('/riddles')
def getRiddles():
  return riddles.get()


@app.get('/riddles/{id}')
def getRiddle(id):
  return riddles.getRiddle(id)


@app.put('/riddles/alter/{id}')
def putRiddle(id, alterRiddle: Riddle):
  newRiddle = alterRiddle.__dict__
  return riddles.alterRiddle(id, newRiddle)


@app.post('/riddles/set')
def postRiddle(riddle: Riddle):
  return riddles.setNewRiddle(riddle.__dict__)
