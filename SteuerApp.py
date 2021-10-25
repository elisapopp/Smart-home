class SteuerApp:
#Aufrufer
  
  def __init__(self): 
    self.__history = []
  
  def addBefehl(self, befehl):
    self.__history.append(befehl)
   
  def removeBefehl(self, befehl):
    self.__history.remove(befehl)

  def aktionAusfuehren(self, befehl):
    self.__history.append(befehl)
    befehl.ausfuehren()