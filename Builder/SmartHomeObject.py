class SmartHomeObject:
   def __init__(self):
      self.__stromverbrauch = None
      self.__sensorTyp = None
      self.__steuergeraet = None
      self.__produktID = None

   def setStromverbrauch(self, stromverbrauch):
      self.__stromverbrauch = stromverbrauch

   def setSensorTyp(self, sensorTyp):
      self.__sensorTyp = sensorTyp

   def setSteuergeraet(self, steuergeraet):
      self.__steuergeraet = steuergeraet

   def setProduktID(self, produktID):
      self.__produktID = produktID

   def specification(self):
      print("Stromverbrauch: %d" % self.__stromverbrauch + "w/h")
      print("Sensor-Typ: " + self.__sensorTyp)
      print("Steuergerät: " + self.__steuergeraet)
      print("Produkt-ID: %d" % self.__produktID)