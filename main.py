from FernseherBuilder import *
from LampenBuilder import *
from RolladenBuilder import *
from Director import *
from Rolladen import *
from Fernseher import *
from Lampen import *

def main():

   print("------------------------START----------------------------")
   print("")

   director = Director()

   lampenBuilder = LampenBuilder()
  
   print("Lampe wird erzeugt...")
   director.setBuilder(lampenBuilder)
   lampe = director.getSmartHomeObject()
   lampe.specification()
   print("")
   neueLampe = Lampen(lampe)
   neueLampe.einschalten()
   neueLampe.ausschalten()
   print("")
   print("---------------------------------------------------------------")

   rolladenBuilder = RolladenBuilder()
  
   print("Rolladen wird erzeugt...")
   director.setBuilder(rolladenBuilder)
   rolladen = director.getSmartHomeObject()
   rolladen.specification()
   print("")
   neuerRolladen = Rolladen(rolladen)
   neuerRolladen.hochfahren()
   neuerRolladen.runterfahren()
   print("")
   print("---------------------------------------------------------------")

   fernseherBuilder = FernseherBuilder()
  
   print("Fernseher wird erzeugt...")
   director.setBuilder(fernseherBuilder)
   fernseher = director.getSmartHomeObject()
   fernseher.specification()
   print("")
   neuerFernseher = Fernseher(fernseher)
   neuerFernseher.einschalten()
   neuerFernseher.umschalten()
   neuerFernseher.ausschalten()
   print("")
   print("------------------------END----------------------------")


if __name__ == "__main__":
   main()