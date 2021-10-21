from SmartHomeObject import *

class Lampen(SmartHomeObject):
  """Test instanciation of Lampe.
  
    >>> type(Lampen("Lampen"))
    <class 'Lampen.Lampen'>

    Test einschalten() of Lampen.
    >>> Lampen("L").einschalten()
    Lampe schaltet sich ein

    Test ausschalten() of Lampen.
    >>> Lampen("L").ausschalten()
    Lampe schaltet sich aus
  """

  def __init__(self, SmartHomeObject):
    SmartHomeObject.__init__()

  def einschalten(self):
    print("Lampe schaltet sich ein")

  def ausschalten(self):
    print("Lampe schaltet sich aus")
