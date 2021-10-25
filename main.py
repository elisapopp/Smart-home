from FernseherBuilder import *
from LampenBuilder import *
from RolladenBuilder import *
from Director import *
from Rolladen import *
from Fernseher import *
from Lampen import *
from Kompositum import *
from FernseherKnopf import *
from SteuerApp import *

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

   print("Lampe 2 wird erzeugt...")
   director.setBuilder(lampenBuilder)
   lampe = director.getSmartHomeObject()
   lampe.specification()
   print("")
   neueLampe2 = Lampen(lampe)
   neueLampe2.einschalten()
   neueLampe2.ausschalten()
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

   fernseherBuilder = FernseherBuilder()
  
   print("Fernseher wird erzeugt...")
   director.setBuilder(fernseherBuilder)
   fernseher = director.getSmartHomeObject()
   fernseher.specification()
   print("")
   neuerFernseher = Fernseher(fernseher)
   print("")

   #Wurzel erstellen
   kompositumSHObject = Kompositum()
   #Blätter einfügen
   kompositumSHObject.addSmartHomeObject(neueLampe)
   kompositumSHObject.addSmartHomeObject(neuerRolladen)
   kompositumSHObject.addSmartHomeObject(neuerFernseher)

  #Unter-Komposita erstellen
   KompositumRolladen = Kompositum()
   KompositumRolladen.addSmartHomeObject(neuerRolladen)
   KompositumFernseher = Kompositum()
   KompositumFernseher.addSmartHomeObject(neuerFernseher)
   KompositumLampe = Kompositum()
   KompositumLampe.addSmartHomeObject(neueLampe)
   KompositumLampe.addSmartHomeObject(neueLampe2)

   # Unter-Komposita in Wurzel einfügen
   kompositumSHObject.addSmartHomeObject(KompositumRolladen)
   kompositumSHObject.addSmartHomeObject(KompositumFernseher)
   kompositumSHObject.addSmartHomeObject(KompositumLampe)

   KompositumFernseher.stromverbrauchZuruecksetzen()
   KompositumLampe.stromverbrauchZuruecksetzen()
   KompositumRolladen.stromverbrauchZuruecksetzen()
   kompositumSHObject.stromverbrauchZuruecksetzen()

   import doctest
   #doctest.IGNORE_EXCEPTION_DETAIL
   doctest.testmod()
   print("just test doctest")

   # Kommando Entwurfsmuster

   fernseherKnopf = FernseherKnopf(neuerFernseher)

   steuerApp = SteuerApp()
   steuerApp.aktionAusfuehren(fernseherKnopf)
   steuerApp.aktionAusfuehren(fernseherKnopf)
   

   print("------------------------END----------------------------")


if __name__ == "__main__":
   main()
   