class SmartHomeObject:

    def __init__(self):
      self._stromverbrauch = None
      self._sensorTyp = None
      self._steuergeraet = None
      self._produktID = None

    def setStromverbrauch(self, stromverbrauch):
      self._stromverbrauch = stromverbrauch

    def setSensorTyp(self, sensorTyp):
      self._sensorTyp = sensorTyp

    def setSteuergeraet(self, steuergeraet):
      self._steuergeraet = steuergeraet

    def setProduktID(self, produktID):
      self._produktID = produktID

    def specification(self):
      print("Stromverbrauch: %d" % self._stromverbrauch + "w/h")
      print("Sensor-Typ: " + self._sensorTyp)
      print("Steuergerät: " + self._steuergeraet)
      print("Produkt-ID: %d" % self._produktID)