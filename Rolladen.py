from SmartHomeObject import *
#Blatt
class Rolladen(SmartHomeObject): 
  """
    Test hochfahren()
    >>> Rolladen("TestRolladen").hochfahren()
    Rolladen fährt hoch

    Test runterfahren()
    >>> Rolladen("TestRolladen").runterfahren()
    Rolladen fährt runter
    """

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()


  def hochfahren(self):
    print("Rolladen fährt hoch")


  def runterfahren(self):
    print("Rolladen fährt runter")
