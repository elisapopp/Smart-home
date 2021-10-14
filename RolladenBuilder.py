from Builder import *

class RolladenBuilder(Builder):
  
   def getStromverbrauch(self):
      self.stromverbrauchinkwh = 10
      return self.stromverbrauchinkwh
   
   def getSensorTyp(self):
      self.sensorTypname = "Lichtsensor"
      return self.sensorTypname
   
   def getSteuergeraet(self):
      self.steuergeraetname = "Lichtsteuergerät"
      return self.steuergeraetname

   def getProduktID(self):
      self.produktIDnummer = 100002
      return self.produktIDnummer