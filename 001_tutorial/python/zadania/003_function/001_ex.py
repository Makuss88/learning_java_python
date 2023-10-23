# 01. Write a function that computes the factorial of a number.
# The function should take the number as a parameter and return the factorial value.
"""
def showFactorialNumber(num: int):
    factory_number: int = 1

    for i in range(1, num + 1):
        factory_number *= i
        i += 1

    return factory_number


number = int(input("Show Number: "))

print(showFactorialNumber(number))
"""

# 02.  Write a function that computes the sum of all digits.
# Pass the number as a parameter and return the computed sum
"""
def sumNumber(*nums):
    sum: int = 0
    
    for n in nums:
        sum += n

    return sum


print(sumNumber(1, 3, 5))
print(sumNumber(1, 3, 5, 11))
"""

# 03. Write a function that checks if a number is prime or not.
# Pass the number as a parameter and return True if the number is prime, otherwise return False.
"""
def isPrime(num: int):
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return True


number = int(input("Show Number: "))

if isPrime(number):
    print("YES!!")
else:
    print("nope...")
"""

# 04. Write a function that prints the table of a number.
# Pass the number as a parameter to the function.
"""
def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


n = int(input("Input a number: "))
table(n)
"""

# 05. Write a function that computes the simple interest.
# Pass the principal amount, the rate and the time as parameters to the function.
"""
def simple_interest(z, x, y):
    return (z * x * y) / 100


p = float(input("Input a prinicpal: "))
t = float(input("Input a time: "))
r = float(input("Input a rate: "))

result = simple_interest(p, t, r)
print("The simple interest is - %.2f" % result)
"""

# 06. Write a function that converts Celsius reading to Fahrenheit reading.
# Read the Celsius value from the user in the function and also print the Fahrenheit reading in the function itself.
"""
def celsiusToFahrenheit(c):
    f = (c * 1.8) + 32
    return f


celc = int(input("Enter the value of celsius:"))

fahren = celsiusToFahrenheit(celc)
print("The Fahrenheit is:", fahren)
"""

# 07. Design a function having no parameters and no return statement
"""
def tellMe():
    print("I LOVE PYTHON!")


tellMe()
"""

# 08. Design a function having parameters and no return statement
"""
def my_function(language="PYTHON"):
    print("I LOVE " + language)


my_function("JAVA")
my_function("JavScript")
my_function()
my_function("PHP")
"""

# 09. Design a function having no parameters but a return statement
"""
def print_love():
    return "I love Python 3.0"


print(print_love())
"""


# 10. Design a function having both parameters and return statement
"""
def whichNumberIsBigger(num1, num2):
    if num1 == num2:
        return "the same"
    elif num1 > num2:
        return "num1 is bigger"
    else:
        return "num2 is bigger"


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print(whichNumberIsBigger(num1, num2))
"""
