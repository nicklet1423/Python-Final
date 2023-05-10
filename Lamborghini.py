#----importing------#
import sys
class Lamborghini():
    #-----------------------Functions-------------------------#
    def __init__(self):
        self._color = " "
        self._speed = 50
        self._luxury = "\nLevels of Interior Luxury: [Lv1], [Lv2], [Lv3]"
        self._year = 0
        self._speedlimit = 0

    #-------Adding Speed, Grabbing Speed, Removing Speed-------#
    def addSpeed(self):
        while True:
            self._speed = self._speed + 50
            if self._speed < self._speedlimit:
                return [self._speed]
            else:
                self._speed >= self._speedlimit
                print("You are stopped by police.")
                sys.exit()
                

                





            #if  self._speed = speed
                #self._speed < self._speedlimit:
                #self._speed += 50
            #else:
                #self._speed = self._speedlimit
                #print("You have crashed and died.")
            #exit()
            
    def getSpeed(self):
        while True:
            if self._speed <= 0:
                print("You are at a complete stop.")
                sys.exit()
            else:  
                self._speed = self._speed + 0
            return self._speed
    
    def removeSpeed(self):
        self._speed -= 50
    #-------------------COLOR------------------------#
    def getColor(self):
        return self._color
    def setColor(self, color):
        self._color = color
    #------------------Luxury Level------------------#
    def getLuxury(self):
        return self._luxury
    def setLuxury(self, luxury):
        self._luxury = luxury
    #-----------------Year On Car-------------------#
    def getYear(self):
        return int(self._year)
    def setYear(self, year):
        self._year = year
    #-----------------Speed Limit-------------------#
    def getSpeedLimit(self):
        return int(self._speedlimit)
    def addSpeedLimit(self, speedlimit):
        self._speedlimit = speedlimit
        speedlimit + 100
    #---------------Nitro Mode---------------------#
    def takeoff(self):
        self._speed + 100
