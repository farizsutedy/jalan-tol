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

    def checkData(self):
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")
        carNum = int(len(self.carList))
        busNum = int(len(self.busList))
        truckNum = int(len(self.truckList))
        print ("",carNum ,"\t\t", busNum , "\t\t " , truckNum)
        print("---------------------")

    def checkRevenue(self):
        if int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0 :
            print("Total Revenue : " ,"RP.0")
        else :
            carNum = int(len(self.carList))
            busNum = int(len(self.busList))
            truckNum = int(len(self.truckList))
            revenue = carNum * self.priceCar + busNum * self.priceBus + truckNum * self.priceTruck
            print("\nTotal Revenue : " ,"RP." ,revenue,"\n")

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

a = Vehicle("Vehicle")

while True :

        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 9000)")
        print("4. \tCheck Data")
        print("5. \tTotal Revenue")
        print("6. \tStop Program")
        choice=int(input("Enter choice: "))
        if choice == 1:
            a.CarIn()
        if choice == 2:
            a.BusIn()
        if choice == 3:
            a.TruckIn()
        if choice == 4:
            a.checkData()
        if choice == 5:
            a.checkRevenue()
        if choice == 6:
            print("Program Has Been Stop")
            break

