#Import Math Function
import math


#Ask The Question
while True:
    printMaterial = input("Are you using resin(r) or filament(f)? ")

#Formula for cost of Resin Print

    if printMaterial == ("r"):
        res_x = float(input("Please enter the amount of resin in grams required for print: "))
        res_y = float(input("How many grams come in the bottle of resin you are using (500, 1000, etc)?"))
        res_cost = float(input("Please enter the cost of that bottle of resin: $"))
        res_total = (res_x/res_y*res_cost)
        shopCost = float(input("How much is the shop rate or enter zero: $ "))
        shopHours = float(input("How many shop hours beyond print time? "))
#resin print code
        print("Amount of bottle of resin used: ",(res_x/res_y),"%")
        print("Cost of print: $ ",format(res_total, '.2f'))
        shopTotal_2 = shopCost * shopHours + res_total
        print("The total cost of your project is: $", format(shopTotal_2, '.2f'))
        print("\n")
        try_again = input("\n     Do you want another quote? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
                break
    elif printMaterial == ("f"):
#Formula for cost of PLA Print
        pla_x = float(input("Please enter the amount of filament in grams required for print: "))
        pla_z = float(input("How many spools will be used? "))
        pla_y = float(input("How many grams per spool (250, 500, 1000, etc)? "))
        pla_cost = float(input("Please enter the cost of all spools of filament: $"))
        pla_runtime = float(input("How long is the printer expected to run in hours? "))
        pla_runCost = (pla_runtime*500/1000*.11)
        pla_total = (pla_x/(pla_z*pla_y)*pla_cost*+pla_runCost)
        shopCost = float(input("How much is the shop rate or enter zero: $ "))
        shopHours = float(input("How many shop hours beyond print time? "))
#Filament print code
        print("Amount of spool of filament being used: ",(pla_x/pla_y*pla_z),"%")
        print("Cost of print: $ ",format(pla_total, '.2f'))
        shopTotal_2 = shopCost * shopHours + pla_total
        print("     The total cost of your project is: $", format(shopTotal_2, '.2f'))
        print("(Cost of print runtime based on national average energy cost of $0.11 cents per kilowatt hour)")
        print("\n")
        try_again = input("\n     Do you want another quote? (Press Enter for another or (n) to quit)\n")
        if try_again.lower() == "n":
            break
input("     Press Enter to Exit.")  
