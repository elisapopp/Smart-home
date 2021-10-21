from SmartHomeObject import *

class Fernseher(SmartHomeObject):

  """
  Test einschalten()
  >>> Fernseher("TestFernseher").einschalten()
  TV schaltet sich ein

  Test ausschalten()
  >>> Fernseher("TestFernseher").ausschalten()
  TV schaltet sich aus

  Test umschalten()
  >>> Fernseher("TestFernseher").umschalten()
  TV schaltet um auf ein wichtiges Fussballspiel

  """

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()

  def einschalten(self):  
    print("TV schaltet sich ein")

  def ausschalten(self):
    print("TV schaltet sich aus")

  def umschalten(self):
    print("TV schaltet um auf ein wichtiges Fussballspiel")