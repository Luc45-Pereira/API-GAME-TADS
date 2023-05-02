class Riddle():

  def __init__(self):
    self.riddle = []

  def setNewRiddle(self, question: dict) -> bool:
    self.riddle.append(question)
    return True

  def get(self) -> dict:
    return self.__dict__

  def getRiddle(self, questionId: int):
    for id, riddle in enumerate(self.riddle):
      if (id == questionId):
        return riddle.__dict__
    return False

  def alterRiddle(self, riddleId: int, newRiddle: dict):
    for id, riddle in enumerate(self.riddle):
      if (id == riddleId):
        riddle = newRiddle
        return self.__dict__
    return False
