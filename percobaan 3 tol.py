print ("================================================================================" 
       "\n\t\t\t\t\t\t\tToll Payment Systems" 
       "\n\t\t\t\t\t\t\tPT Jasa Marga, Tbk."
      "\n================================================================================")

def printMenu():
    while True:
        print("Which Toll Gate ? :")
        print("1. Tol jagorawi")
        print("2. Pondok Aren")
        print("3. Check Grand Total Revenue")
        print("4. Stop Program")
        choice=int(input("Enter Choice:"))
        if choice == 1:
            print1()
        if choice == 2:
            print2()
        if choice == 3:
            a.checkTotalRevenue()
        if choice == 4:
            print("Program Has Been Stopped")
            break


def print1():
    while True :
        print("Location Gate : jagorawi")
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 6000)")
        print("2. \tBus\t\t(RP 8000)")
        print("3. \tTruck\t(RP 9000)")
        print("4. \tTotal Revenue")
        print("5. \tChange Gate Location")
        print("6. \tStop Program")
        choice=int(input("Enter choice: "))
        if choice == 1:
            a.CarGoIn()
        if choice == 2:
            a.BusGoIn()
        if choice == 3:
            a.TruckGoIn()
        if choice == 4:
            a.checkRevenue()
        if choice == 5:
            printMenu()
        if choice == 6:
            print("Program Has Been Stop")
            break

def print2():
    while True :
        print("Location Gate : Pondok Aren")
        print("Category of Vehicle :")
        print("1. \tCar\t\t(RP 18000)")
        print("2. \tBus\t\t(RP 20000)")
        print("3. \tTruck\t(RP 25000)")
        print("4. \tTotal Revenue")
        print("5. \tChange Gate Location")
        print("6. \tStop Program")
        choice=int(input("Enter choice: "))
        if choice == 1:
            a.CarGoIn2()
        if choice == 2:
            a.BusGoIn2()
        if choice == 3:
            a.TruckGoIn2()
        if choice == 4:
            a.checkRevenue2()
        if choice == 5:
            printMenu()
        if choice == 6:
            print("Program Has Been Stop")
            break

class TollGate():
    def __init__(self,type):
        self.priceCar = 6000
        self.priceBus = 8000
        self.priceTruck = 10000
        self.priceCar2 = 18000
        self.priceBus2 = 20000
        self.priceTruck2 = 25000
        self.busList = []
        self.carList = []
        self.truckList = []
        self.busList2 = []
        self.carList2 = []
        self.truckList2 = []
        self.type = type

    def checkRevenue(self):
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")
        carNum = int(len(self.carList))
        busNum = int(len(self.busList))
        truckNum = int(len(self.truckList))
        print ("",carNum ,"\t\t", busNum , "\t\t " , truckNum)
        print("---------------------\n")
        if int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0 :
            print("Total Revenue : " ,"RP.0")
        else :
            carNum = int(len(self.carList))
            busNum = int(len(self.busList))
            truckNum = int(len(self.truckList))
            revenue = carNum * self.priceCar + busNum * self.priceBus + truckNum * self.priceTruck
            print("Total Revenue : " ,"RP." ,revenue,"\n")
            return revenue

    def checkRevenue2(self):
        print("---------------------")
        print("Car\t\tBus\t\tTruck")
        print("---------------------")
        carNum2 = int(len(self.carList2))
        busNum2 = int(len(self.busList2))
        truckNum2 = int(len(self.truckList2))
        print ("",carNum2 ,"\t\t", busNum2 , "\t\t " , truckNum2)
        print("---------------------\n")
        if int(len(self.carList2)) == 0 and int(len(self.busList2)) == 0 and int(len(self.truckList2)) == 0 :
            print("Total Revenue : " ,"RP.0")
        else :
            carNum = int(len(self.carList2))
            busNum = int(len(self.busList2))
            truckNum = int(len(self.truckList2))
            revenue2 = carNum * self.priceCar2 + busNum * self.priceBus2 + truckNum * self.priceTruck2
            print("Total Revenue : " ,"RP." ,revenue2,"\n")
            return revenue2

    def checkTotalRevenue(self):
        if int(len(self.carList2)) == 0 and int(len(self.busList2)) == 0 and int(len(self.truckList2)) == 0 and int(len(self.carList)) == 0 and int(len(self.busList)) == 0 and int(len(self.truckList)) == 0:
            print("\nTotal Revenue : " ,"RP.0\n")
        else :
            totalRevenue = a.checkRevenue() + a.checkRevenue2()
            print("\nTotal Revenue : " ,totalRevenue,"\n")

class Vehicle(TollGate):

    def CarGoIn(self):
        self.carList.append(self.type)
        print("\nFee :",self.priceCar,"\n")

    def BusGoIn(self):
        self.busList.append(self.type)
        print("\nFee :",self.priceBus,"\n")

    def TruckGoIn(self):
        self.truckList.append(self.type)
        print("\nFee :",self.priceTruck,"\n")


    def CarGoIn2(self):
        self.carList2.append(self.type)
        print("\nFee :",self.priceCar2,"\n")
    def BusGoIn2(self):
        self.busList2.append(self.type)
        print("\nFee :",self.priceBus2,"\n")
    def TruckGoIn2(self):
        self.truckList2.append(self.type)
        print("\nFee :",self.priceTruck2,"\n")
a = Vehicle("Vehicle")

printMenu()

