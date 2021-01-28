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
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - int(age)

print(f'You have {years_left * 365} days, {years_left * 52} weeks, and {years_left * 12} months left.')



