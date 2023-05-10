"""
    Name: Final_Vehicle_OOP.py 
    Author: Nicolas Smith
    Purpose: Controlling a vehicle of your choice
    Date: 5/9/2023
"""

#-- Importing Functions --#
import utils
from Lamborghini import Lamborghini

def main():
    #Printing title
    print(utils.title("Lamborghini's In Nebraska"))
    # Naming the class
    cessna = Lamborghini()
    choice = Lamborghini.getSpeed
    #Inputs, color, luxury, model of car
    print(cessna.getColor())
    (cessna.setColor(input("What color of Lamborghini would you like: ")))

    print(cessna.getLuxury())
    (cessna.setLuxury(input("What level of Luxury would you like: ")))

    
    (cessna.setYear(utils.get_int("What Year would you like: ")))

    
    (cessna.addSpeedLimit(utils.get_int("What would you like your speed limit to be: ")))         #2222



    #Printing out the inputs
    print(f"The {cessna.getLuxury()} {cessna.getYear()} {cessna.getColor()} Lamborghini is going {cessna.getSpeed()} mph.")
    

    while choice:

        choice = input("(A)ccelerate  (B)rake  (T)ake Off  (F)ly  or  (E)xit: ")

        if choice == "a":
            cessna.addSpeed()
            print(f"The {cessna.getLuxury()} {cessna.getYear()} {cessna.getColor()} Lamborghini is going {cessna.getSpeed()} mph.")
            continue

        elif choice == "b":
            cessna.removeSpeed()
            print(f"The {cessna.getLuxury()} {cessna.getYear()} {cessna.getColor()} Lamborghini is going {cessna.getSpeed()} mph.")
            continue

        elif choice == "t":
            cessna.takeoff()
            print(f"The {cessna.getLuxury()} {cessna.getYear()} {cessna.getColor()} Lamborghini is going {cessna.getSpeed()} mph.")

        elif choice == "f":
            cessna.fly()
            print(f"The {cessna.getLuxury()} {cessna.getYear()} {cessna.getColor()} Lamborghini is going {cessna.getSpeed()} mph.")

        else:
            break




if __name__ == "__main__":  
    main()