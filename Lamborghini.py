#----importing------#
import sys
from rich.console import Console
from rich.panel import Panel
console = Console()

class Lamborghini():
    #-----------------------Functions-------------------------#
    def __init__(self):
        self._color = " "
        self._speed = 50
        self._luxury = ""
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
                console.print(f"You are stopped by police, You have went to jail👮 for exceeding [bold {self._color}]{self._speedlimit}[/] mph.")
                sys.exit()
                

            
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
        while True:
            self._speed = self._speed + 100
            if self._speed < self._speedlimit:
                return [self._speed]
            else:
                self._speed >= self._speedlimit
                print(f"You are stopped by police, You have went to jail👮 for exceeding [bold {self._color}]{self._speedlimit}[/] mph.")
                sys.exit()
    #---------------Flying Mode-----------------------------#
    def fly(self):
        while True:
            self._speed = self._speed + 600
            if self._speed < self._speedlimit:
                return [self._speed]
            else:
                self._speed >= self._speedlimit
                console.print(f"You got stopped by the [bold {self._color}]Galactic Federation[/] of space, You have went to jail👮 for exceeding [bold {self._color}]{self._speedlimit}[/] mph.")
                sys.exit()