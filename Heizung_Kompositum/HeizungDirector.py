from Heizung import *

class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getSmartHomeObject(self):
      smartHomeObject = SmartHomeObject()
      
      stromverbrauch = self.__builder.getStromverbrauch()
      smartHomeObject.setStromverbrauch(stromverbrauch)
      
      sensorTyp = self.__builder.getSensorTyp()
      smartHomeObject.setSensorTyp(sensorTyp)

      steuergeraet = self.__builder.getSteuergeraet()
      smartHomeObject.setSteuergeraet(steuergeraet)

      produktID = self.__builder.getProduktID()
      smartHomeObject.setProduktID(produktID)
      return smartHomeObject