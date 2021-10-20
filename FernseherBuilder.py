from Builder import *
from Fernseher import *
from SmartHomeObject import *

class FernseherBuilder(Builder):

  self = Fernseher()
  
  def getStromverbrauch(self):
    self.stromverbrauchinkwh = 100
    return self.stromverbrauchinkwh
   
  def getSensorTyp(self):
    self.sensorTypname = "Fernbedienungssensor"
    return self.sensorTypname
   
  def getSteuergeraet(self):
    self.steuergeraetname = "Reciever"
    return self.steuergeraetname

  def getProduktID(self):
    self.produktIDnummer = 100003
    return self.produktIDnummer