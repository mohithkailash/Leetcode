class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.count = [big,medium,small]
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.c1 == self.count[0]:
                return False
            else:
                self.c1 += 1
                return True
        elif carType == 2:
            if self.c2 == self.count[1]:
                return False
            else:
                self.c2 += 1
                return True
        else:
            if self.c3 == self.count[2]:
                return False
            else:
                self.c3 += 1
                return True
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)