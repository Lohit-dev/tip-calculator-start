#  This is program 1 of 100 days of code 
#  Author - Lohit Sharma
#  This program will ask user for total amount of bill and total tip and number 
#  of people they want to split between 
#  It will tell how much money does every person owes

#Ask user for all the inputs
total_bill = float(input("How much was the total bill? \n"))
tip_percent = int(input("How much tip would you like to add? 10,15 or 20? \n"))
total_people = int(input("How many people were dining? \n"))

#calculate the total bill including the tip
total_bill += tip_percent/100 * total_bill

print(f"Each person owes {total_bill/total_people} dollars")