# 01. Write a Python program to check if the a number is prime or not.
"""
def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = int(input("Give number: "))

if is_prime(num):
    print("TAK")
else:
    print("NIE")
"""

# 02. Write a Python program to print the following series:
# a) 1,4,7,10….n terms
# b) 1,-4,7,-10,…,n terms
"""
num = int(input("Give number: "))

list = []
list_with_minus = []
i = 0

for i in range(i, num):
    list.append(i * 3 + 1)
    if i % 2 == 0:
        list_with_minus.append(i * 3 + 1)
    else:
        list_with_minus.append(-(i * 3 + 1))
print(list, list_with_minus)
"""

# 03. Write a Python program to read the three sides of a triangle and print whether the triangle is equilateral, isosceles or scalene
"""
side_1 = int(input("Show side_1: "))
side_2 = int(input("Show side_2: "))
side_3 = int(input("Show side_3: "))


def which_trangle(s_1: int, s_2: int, s_3: int):
    if s_1 + s_2 <= s_3 or s_2 + s_3 <= s_1 or s_1 + s_3 <= s_2:
        print("wrong sides!")
        return False
    if s_1 == s_2 == s_3:
        print("equilateral")
    elif s_1 == s_2 or s_1 == s_3 or s_2 == s_3:
        print("isotonic")
    else:
        print("scalane")


which_trangle(side_1, side_2, side_3)
"""

# 04.Write a  Python program to print the second largest number from 3 numbers entered by the user.
"""
num_1 = int(input("Show number1: "))
num_2 = int(input("Show number2: "))
num_3 = int(input("Show number3: "))

list = [num_1, num_2, num_3]
list.sort()
print("second is ", list[1])
"""

# 05. Write a Python program to make Fibonacci sequence:
"""
def fibonacci_list(num):
    count = []
    a, b = 0, 1

    for i in range(0, num):
        count.append(a)
        a, b = b, a + b
        i += 1
    return count


num = int(input("Show number: "))
print(fibonacci_list(num))
"""

# 06. Write a Python program to print the sum of the following sequence:
"""
def fibonacci_sum(n):
    sum = 0
    a, b = 0, 1

    for _ in range(n):
        sum += a
        a, b = b, a + b
    return sum


n = int(input("Enter the number of terms: "))
result = fibonacci_sum(n)
print("The sum of the Fibonacci sequence up to the", n, "term(s) is:", result)
"""

# 06. Write a Python program to compute the factorial of a number.
"""
def show_factorial(num):
    if num < 0:
        print("OMG - negative numbers...")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial


num = int(input("Enter a number: "))
print("The factorial of", num, "is", show_factorial(num))
"""

# 07. Write a Python program to check if a number is an Armstrong number or not.
"""
def count_digits(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def sum(n):
    i = count_digits(n)
    s = 0
    while n > 0:
        digit = n % 10
        n //= 10
        s += pow(digit, i)
    return s


num = int(input("Enter a number: "))
arm_num = sum(num)

if arm_num == num:
    print("YES!")
else:
    print("NO!")
"""

# 08. Write a Python program to print the following pattern

"""
def print_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)


n = int(input("Enter a number: "))
print_pattern(n)
"""
