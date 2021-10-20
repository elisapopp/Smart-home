from Builder import *

class LampenBuilder(Builder):
  
   def getStromverbrauch(self):
      self.stromverbrauchinkwh = 400
      return self.stromverbrauchinkwh
   
   def getSensorTyp(self):
      self.sensorTypname = "Lichtsensor"
      return self.sensorTypname
   
   def getSteuergeraet(self):
      self.steuergeraetname = "Lampensteuergerät"
      return self.steuergeraetname

   def getProduktID(self):
      self.produktIDnummer = 100001
      return self.produktIDnummer