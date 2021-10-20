from SmartHomeObject import *

class Fernseher(SmartHomeObject): 

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()

  def einschalten(self):
    print("TV schaltet sich ein")

  def ausschalten(self):
    print("TV schaltet sich aus")

  def umschalten(self):
    print("TV schaltet um auf ein wichtiges Fussballspiel")