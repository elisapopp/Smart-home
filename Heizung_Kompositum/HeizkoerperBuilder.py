from HeizungBuilder import *

class HeizkoerperBuilder(HeizungBuilder):

   def setZimmer(self):
      self.zimmer = 400
      return self.stromverbrauchinkwh
   
   def sensorTypBestimmen(self):
      self.sensorTypname = "Lichtsensor"
      return self.sensorTypname
   
   def BedienungEinstellen(self):
      self.steuergeraetname = "Lampensteuergerät"
      return self.steuergeraetname

   def getProduktID(self):
      self.produktIDnummer = 100001
      return self.produktIDnummer