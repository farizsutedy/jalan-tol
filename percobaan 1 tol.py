print ("================================================================================" 
       "\n\t\t\t\t\t\t\tToll Payment Systems" 
       "\n\t\t\t\t\t\t\tPT Jasa Marga, Tbk."
      "\n================================================================================")


class TollGate():
    def __init__(self,type):
        self.priceCar = 6000
        self.priceBus = 8000
        self.priceTruck = 10000
        self.busList = []
        self.carList = []
        self.truckList = []
        self.type = type


class Vehicle(TollGate):

    def CarIn(self):
        self.carList.append(self.type)
        print("\nFee :",self.priceCar,"\n")

    def BusIn(self):
        self.busList.append(self.type)
        print("\nFee :",self.priceBus,"\n")

    def TruckIn(self):
        self.truckList.append(self.type)
        print("\nFee :",self.priceTruck,"\n")

x = Vehicle("Vehicle")

while True :

        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 9000)")
        print("4. \tStop Program")
        choice=int(input("Enter choice: "))
        if choice == 1:
            x.CarIn()
        if choice == 2:
            x.BusIn()
        if choice == 3:
            x.TruckIn()
        if choice == 4:
            print("Program Stopped")
            break

