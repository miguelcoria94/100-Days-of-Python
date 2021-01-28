# GOAL: Makeatipcalculator

# print(len(33))

# typeerror when you pass a number to the len function

# print("Hello"[0])

# just explaining how we start indexing at 0

# print("123" + "345")

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# print(int(str(two_digit_number)[0]) + int(str(two_digit_number)[1]))

# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# print(round(float(weight) / (float(height) * float(height))) )

# print(round(8 // 3))
# print(round(8 / 3, 3))

# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# years_left = 90 - int(age)

# print(f'You have {years_left * 365} days, {years_left * 52} weeks, and {years_left * 12} months left.')


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator!")
total_bill = input("what was the total bill? $")
percentage = input("what percentage are you tipping? 10%, 12% or 15%?")
party_size = input("how many people are splitting the bill?")

actual_total = float(total_bill) + (float(total_bill) * (int(percentage) / 100))

split_amount = round(actual_total / int(party_size), 2)

print(f'Each person will have to pay: ${split_amount}')


