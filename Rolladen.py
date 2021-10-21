from SmartHomeObject import *
#Blatt
class Rolladen(SmartHomeObject): 

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()


  def hochfahren(self):
    print("Rolladen fährt hoch")


  def runterfahren(self):
    print("Rolladen fährt runter")
