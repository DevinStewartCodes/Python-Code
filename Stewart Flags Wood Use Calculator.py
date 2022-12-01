#import
import math
#Calculate cost of wood
while True:
    boardLength = float(input("     How long is the wood in inches? "))
    boardWidth = float(input("     How wide is the wood in inches? "))
    boardThickness = float(input("     How thick is the board in inches or decimals? "))
    boardFoot = boardLength * boardWidth * boardThickness / 144
    wood = float(input("     How much is the wood per foot? $ "))
    woodCost = boardFoot * wood
    print("     The cost of your wood is $", format(woodCost, '.2f'))
    print("\n")
#cost of laser
    laserUse = input("     Was the laser used on this project?(y) or (n) ")
    if laserUse == ("y"):
        watts = float(input("     What is the wattage of the laser? "))
        hoursUse = float(input("     How many hours was the laser in use? "))
        kwHR = float(0.15)
        laserCost = watts * hoursUse / 1000 * kwHR
        print("     Your laser cost is: $", format(laserCost, '.2f'))
        print("\n")
        shopCost = float(input("     How much is the shop rate or enter zero: $ "))
        shopHours = float(input("     How many shop hours? "))
        shopTotal_1 = shopCost * shopHours + woodCost + laserCost
        print("     The total cost of your project is: $", format(shopTotal_1, '.2f'))
        try_again = input("\n     Do you want another quote? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
            break
#cost no laser    
    elif laserUse == ("n"):
        shopCost = float(input("      How much is the shop rate or enter zero: $ "))
        shopHours = float(input("     How many shop hours? "))
        shopTotal_2 = shopCost * shopHours + woodCost
        print("     The total cost of your project is: $", format(shopTotal_2, '.2f'))
        try_again = input("\n     Do you want another quote? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
            break
input("     Press Enter to Exit.")    
        
      

