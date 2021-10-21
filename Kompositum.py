from SmartHomeObject import *
#Kompositum
class Kompositum():

  def __init__(self): 
        self.__shobject = []
  
  def addSmartHomeObject(self, smartHomeObject):
    self.__shobject.append(smartHomeObject)
   
  def removeSmartHomeObject(self, smartHomeObject):
    self.__shobject.remove(smartHomeObject)
    
  def stromverbrauchZuruecksetzen(self):
    for obj in self.__shobject: 
      if isinstance(obj, Kompositum):
        obj.stromverbrauchZuruecksetzen()
      else:
        obj.setStromverbrauch(0)
        print("Stromverbrauch wurde zurückgesetzt auf: " + str(obj.getStromverbrauch()) + " w/h")

