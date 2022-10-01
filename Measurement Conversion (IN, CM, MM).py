#Measurment table
import math


while True:
    measUsing = input("Are you converting INCHES(in), CENTIMETERS(cm), or MILLIMETERS(mm)? ")
    if measUsing == ("in"):
        inch = float(input("Please input the number of inches you are converting: "))
        cmci = inch * 2.54
        mmci = inch * 25.4
        print("You\'re conversion for ",inch,"inches is: ")
        print("Centimeters: ", cmci)
        print("Millimeters: ", mmci)
        try_again = input("\n     Do you want another conversion? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
                break
    elif measUsing == ("cm"):
        centi = float(input("Please input the number of centimeters you are converting: "))
        incc = centi * 0.393701
        mmccm = centi * 10
        print("You\'re conversion for ",centi,"centimeters is: ")
        print("Inches: ", incc)
        print("Millimeters: ", mmccm)
        try_again = input("\n     Do you want another conversion? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
                break
    elif measUsing == ("mm"):
        milli = float(input("Please input the number of millimeters you are converting: "))
        incmm = milli * 0.0393701
        cncmm = milli * 0.1
        print("You\'re conversion for ",milli,"millimeters is: ")
        print("Inches: ", incmm)
        print("Centimeters: ", cncmm)
        try_again = input("\n     Do you want another conversion? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
                break
    else:
        print("\n")
        print("Input not understood. Please try again\n")
            
input("     Press Enter to Exit.") 
                     

        
