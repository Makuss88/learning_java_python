# 01. Write a Python program to check if a year is a leap year or not.
"""
year = int(input("shiow year: "))
if year % 4 == 0:
    print("leap")
else:
    print("not leap")
"""

# 02. Write a Python program to read a number from the user and print the reversed number.
"""
num = int(input("shiow number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
"""

# 03. Write a Python program to find the largest of 3 numbers.
"""
num_1 = int(input("Show number1: "))
num_2 = int(input("Show number2: "))
num_3 = int(input("Show number3: "))

max = 0

if num_1 > num_2 and num_1 > num_3:
    max = num_1
elif num_2 > num_1 and num_2 > num_3:
    max = num_2
# elif num_3 > num_1 and num_3 > num_2:
else:    
    max = num_3
print("Max Number: " + str(max))
"""

# 05. Write a Python program that inputs three numbers and calculates two sums as per this:
"""
num_1 = int(input("Show number1: "))
num_2 = int(input("Show number2: "))
num_3 = int(input("Show number3: "))

sum_1 = num_1 + num_2 + num_3

numbers_set = {num_1, num_2, num_3}
sum_2 = 0
for i in numbers_set:
    sum_2 += i


# if num_1 != num_2 and num_1 != num_3 and num_2 != num_3:
#     sum_2 = num_1 + num_2 + num_3
# elif num_1 == num_2 and num_1 != num_3:
#     sum_2 = num_1 + num_3
# elif (num_1 == num_3 or num_2 == num_3) and num_1 != num_2:
#     sum_2 = num_1 + num_2
# else:
#     sum_2 = num_1

print(sum_1, sum_2)
"""

# 06. Write a Python program to check if a number is divisible by another number of not.
"""
num = int(input("Enter the number whose divisibility needs to be checked:"))
div = int(input("Enter the number with which divisibility needs to be checked:"))

if num % div == 0:
    print("The number is divisible.")
else:
    print("The number is not divisible.")
"""

# 07. Write a Python program to read three numbers and print them in ascending order.
"""
num_1 = int(input("Show number1: "))
num_2 = int(input("Show number2: "))
num_3 = int(input("Show number3: "))

if num_1 > num_2:
    num_1, num_2 = num_2, num_1
if num_1 > num_3:
    num_1, num_3 = num_3, num_1
if num_2 > num_3:
    num_2, num_3 = num_3, num_2

print(num_1, "<", num_2, "<", num_3)
"""

# 08.Write a Python program to read today’s date from the user and print how many days are there in the current month.

"""
date_user = input("Introduce date in format DD/MM/YYYY:")


def days_of_month_calculator(day, x, y):
    if x in months_with_31:
        return 31 - day
    elif x in month_with_30:
        return 30 - day
    elif y % 4 == 0:
        return 29 - day
    else:
        return 28 - day


if len(date_user) != 10:
    print("Format doesnt match")
else:
    day = int(date_user[0:2:1])
    month = int(date_user[3:5:1])
    months_with_31 = (1, 3, 5, 7, 8, 10, 12)
    month_with_30 = (4, 6, 9, 11)
    year = int(date_user[6:10:1])
    if (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 0):
        print("Are You crazy??")
    else:
        print(days_of_month_calculator(day, month, year))
"""

# 09. Write a Python program to print the table of a number entered by the user.

"""
how_many_numbers = int(input("How namy numbers??: "))
number_list = []

for num in range(1, how_many_numbers + 1):
    number_list.append(num)

print(number_list)
"""

# 10. Write a Python program to print the sum of first n natural numbers, where n is entered by the user.
""" 
how_many = int(input("How many numbers to adding??: "))
sum = 0

for i in range(1, how_many + 1):
    sum += i

print(sum)
"""

# 11. Write a Python program to calculate and print the sums of odd and even integers of the first n natural numbers.
"""
how_many = int(input("How many numbers to adding??: "))
sum_odd = 0
sum_even = 0

for i in range(1, how_many + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(sum_odd, sum_even)
"""

# 12. Write a Python program to print the following pattern:
# Example: n=5
# * * * * *
# * * * *
# * * *
# * *
# *
"""
num1 = int(input("how many??: "))
for i in range(num1, 0, -1):
    for j in range(i):
        print("* ", end="")
    print()
"""
