class Heizung:
   def __init__(self):
      self.__stromverbrauch = None
      self.__sensorTyp = None
      self.__steuergeraet = None
      self.__produktID = None
      self.__Zimmer = None

   def setZimmer(self, zimmer):
      self.__stromverbrauch = zimmer

   def SensorTypBestimmen(self, sensorTyp):
      self.__sensorTyp = sensorTyp

   def BedienungEinstellen(self, steuergeraet):
      self.__steuergeraet = steuergeraet

   def Ausgabe(self):
      print("Stromverbrauch: %d" % self.__stromverbrauch + "w/h")
      print("Sensor-Typ: " + self.__sensorTyp)
      print("Steuergerät: " + self.__steuergeraet)
      print("Produkt-ID: %d" % self.__produktID)