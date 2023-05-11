"""
    Name: Final_Vehicle_OOP.py 
    Author: Nicolas Smith
    Purpose: Controlling a vehicle of your choice
    Date: 5/9/2023
"""

#-- Importing utils for the int --#
import utils
#-- importing methods and functions ------#
from Lamborghini import Lamborghini
#----------adding color------#
from rich.console import Console
from rich.panel import Panel
console = Console()

def main():
    #Printing title
    console.print(
    Panel.fit(
        " 🏁Lamborghini's In Nebraska 🏎️ ",
        style="bold yellow",
        subtitle="By Lamborghini Incorporated")
)
    # Naming the class
    cessna = Lamborghini()
    choice = Lamborghini.getSpeed
    #-----------input color for car---------------#
    print(cessna.getColor())
    (cessna.setColor(input("What color of Lamborghini would you like: ")))
    #----------------inputing and printing luxury level---------------------#
    print(cessna.getLuxury())
    console.print(f"Levels of Interior Luxury: [bold yellow][Lv1][/], [bold yellow][Lv2][/], [bold yellow][Lv3][/]")
    (cessna.setLuxury(input("What level of Luxury would you like: ")))
    #----------------inputing year of car---------------------#
    (cessna.setYear(utils.get_int("What Year would you like: ")))
    #-----------------inputing speed limit for car--------------------#
    (cessna.addSpeedLimit(utils.get_int("What would you like your speed limit to be: ")))
    #----------------printing out in inputs together---------------------#
    console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
    
    #------------------Loop for the choies to make-------------------#
    while choice:

        choice = input("(A)ccelerate  (B)rake  (T)ake Off  (F)ly  or  (E)xit: ")
        #----------------adding speed---------------------#
        if choice == "a":
            cessna.addSpeed()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
            continue
        #---------------removing speed----------------------#
        elif choice == "b":
            cessna.removeSpeed()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
            continue
        #--------------adding about double speed-----------------------#
        elif choice == "t":
            cessna.takeoff()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
        #----------------adding a airplane amount of speed---------------------#
        elif choice == "f":
            cessna.fly()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
        #---------------Breaking for exit----------------------#
        elif choice == "e":
            console.print(f"[bold {cessna._color}]Thank you for test driving Lamborghini's inventory![/]")
            break
        else:
            break




if __name__ == "__main__":  
    main()