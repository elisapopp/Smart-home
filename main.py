from FernseherBuilder import *
from LampenBuilder import *
from RolladenBuilder import *
from Director import *

def main():

   director = Director()

   lampenBuilder = LampenBuilder()
  
   print("Lampe")
   director.setBuilder(lampenBuilder)
   lampe = director.getSmartHomeObject()
   lampe.specification()
   print("")

   rolladenBuilder = RolladenBuilder()
  
   print("Rolladen")
   director.setBuilder(rolladenBuilder)
   rolladen = director.getSmartHomeObject()
   rolladen.specification()
   print("")

   fernseherBuilder = FernseherBuilder()
  
   print("Fernseher")
   director.setBuilder(fernseherBuilder)
   fernseher = director.getSmartHomeObject()
   fernseher.specification()
   print("")



if __name__ == "__main__":
   main()