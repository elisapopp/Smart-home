from Befehl import *

class FernseherKnopf(Befehl):
#Unterklasse von Befehl

  def __init__(self, fernseher): 
    self.__fernseherAn = False
    self.__fernseher = fernseher
  
  def ausfuehren(self):
    if self.__fernseherAn == False:
      self.__fernseherAn = True
      self.__fernseher.einschalten()
    else:
      self.__fernseherAn = False
      self.__fernseher.ausschalten()
