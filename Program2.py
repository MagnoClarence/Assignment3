#Clarence Magno
#program 2
#Oct 31, 2021

    # Create a program that will ask how many apples and oranges you want to buy.
    # Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
    
    # Constant values so that changing the price will be easy
APPLE_PRICE = 20
ORANGE_PRICE = 25
        
def getQty(fruitName):
        """
            args: takes a string and is used to determine the output of the program
            return: the value of the userInput
        """
        while 1:
                qty = int(input("How many " + fruitName + " do you want to buy?: "))
                if qty < 0:
                        print("You cannot buy negative items.")
                else:
                        break
        return qty
        
print("program 2\n")

    #Step 1: Show how much 1 piece of apple and 1 piece of orange cost.
print(f"₱{APPLE_PRICE} per 1 piece of apple")
print(f"₱{ORANGE_PRICE} per 1 piece of orange\n")

    # Step 2: Ask the user how many apples do they plan to buy.
applesCnt = getQty("apples")

    # Step 3: Ask the user how many oranges do they plan to buy.
orangeCnt = getQty("oranges")
print("\n")

    # Show how many apple and oranges they bought and the total price for each fruit.
print(f"Apples: \n qty: {applesCnt} \n price: ₱{applesCnt * APPLE_PRICE}")    
print(f"Oranges: \n qty: {orangeCnt} \n price: ₱{orangeCnt * ORANGE_PRICE}\n")  

    # Final Step: Display the output in the following format. "The total amount is ______."
print(f"the total amount is ₱{(applesCnt * APPLE_PRICE) + (orangeCnt * ORANGE_PRICE)}")
exit