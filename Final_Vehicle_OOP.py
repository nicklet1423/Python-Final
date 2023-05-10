"""
    Name: Final_Vehicle_OOP.py 
    Author: Nicolas Smith
    Purpose: Controlling a vehicle of your choice
    Date: 5/9/2023
"""

#-- Importing Functions --#
import utils
from Lamborghini import Lamborghini
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
    #Inputs, color, luxury, model of car
    print(cessna.getColor())
    (cessna.setColor(input("What color of Lamborghini would you like: ")))

    print(cessna.getLuxury())
    console.print(f"Levels of Interior Luxury: [bold yellow][Lv1][/], [bold yellow][Lv2][/], [bold yellow][Lv3][/]")
    (cessna.setLuxury(input("What level of Luxury would you like: ")))

    
    (cessna.setYear(utils.get_int("What Year would you like: ")))

    
    (cessna.addSpeedLimit(utils.get_int("What would you like your speed limit to be: ")))



    #Printing out the inputs
    console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
    

    while choice:

        choice = input("(A)ccelerate  (B)rake  (T)ake Off  (F)ly  or  (E)xit: ")

        if choice == "a":
            cessna.addSpeed()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
            continue

        elif choice == "b":
            cessna.removeSpeed()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")
            continue

        elif choice == "t":
            cessna.takeoff()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")

        elif choice == "f":
            cessna.fly()
            console.print(f"Your [bold {cessna._color}]{cessna.getLuxury()}[/] [bold {cessna._color}]{cessna.getYear()}[/] [bold {cessna._color}]{cessna.getColor()}[/] Lamborghini is going [bold {cessna._color}]{cessna.getSpeed()}[/] mph.")

        else:
            break




if __name__ == "__main__":  
    main()