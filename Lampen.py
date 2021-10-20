from SmartHomeObject import *

class Lampen(SmartHomeObject):

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()

  def einschalten(self):
    print("Lampe schaltet sich ein")

  def ausschalten(self):
    print("Lampe schaltet sich aus")
