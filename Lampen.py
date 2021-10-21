from SmartHomeObject import *

class Lampen(SmartHomeObject):
  """Test instanciation of Lampe.

    Test einschalten() of Lampen.
    >>> Lampe().einschalten()
    Lampe schaltet sich ein

    Test ausschalten() of Lampen.
    >>> Lampe().ausschalten()
    Lampe schaltet sich aus
  """

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()

  def einschalten(self):
    print("Lampe schaltet sich ein")

  def ausschalten(self):
    print("Lampe schaltet sich aus")
