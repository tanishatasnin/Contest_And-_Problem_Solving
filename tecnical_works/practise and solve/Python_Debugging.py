
# -----------------------------------------------
# python
# def greet(name):
#     print("Hello, " + name)

# -----------------------------------------------


# numbers = [1, 2, 3, 4, 5]
# print(numbers[4])

 # This will print the last element of the list, which is 5
# -----------------------------------------

# **83.** Find the bug:

# x = 10
# if x == 10:
#     print("x is 10") 
#  # not = , it should be == for comparison, not assignment
# -------------------------------------

# **84.** Find the bug:
# ```python
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)

# it was ar oparetor error 
# ----------------------------------------
# age = int (input("Enter your age: "))

# if age >= 18:
#     print("Adult")

# -------------------------

# def divide(a, b):
#     if b==0:
#         return None
#     else:
#         return a/b
# print(divide(10, 0))
# -----------------------------

# text = "Hello World"
# print(text[10])

# -------------------

# my_dict = {"name": "Alice", "age": 25}
# print(my_dict.get("email", "not found email")) 

# ---------------------

# import math
# num = -1
# if num<0:
#     print("Cannot calculate square root of negative number")
# else:
#     result = math.sqrt(num)
#     print(result)

# -----------------------------------------

# import math
# import cmath
# result = cmath.sqrt(-1)
# print(result)  

# ----------------------------------------

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))

# --------------------------
# x = 5
# y = int("10")
# print(x + y)

# ----------------
# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(total)

# -------------------------

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# num= is_even(4)
# print(num)

# -------------------------

# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()

# # # -----------------------------
# def append_to_list(item, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(item)
#     return my_list
# print(append_to_list(1))
# print(append_to_list(2))
# print(append_to_list(3))
# # -------------------------

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#             self.balance -= amount
#             return self.balance

# account = BankAccount(100)
# print(account.withdraw(60))
# print(account.balance)
# =----------------------------------------------------
# import json

# data = '{"name": "Alice", "age": 25}'
# parsed = json.loads(data)
# print(parsed.get("name"))
# print(parsed.get("email", "not found email"))  # This will print "not found email" since "email" is not in the dictionary

# --------------------------------------------

# def get_average(numbers):
#     if not numbers:
#         return 0 
#     else:
#         total = 0
#         return sum(numbers) / len(numbers)

# print(get_average([2,2,2,2]))

# -----------------------------------------------------
# try:
#     result = 10 / 7
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#     result = None
# finally:
#     print("Result is: " + str(result))

# ---------------------------------------------------

# def process_data(data):
#     result = []
#     for item in data:
#         if item > 0:
#             result.append(item * 2)
#     return result

# numbers = [1, -2, 3, -4, 5]
# result = process_data(numbers)
# print(len(result))

# ----------------------------------------------

# import requests
# try:
#     response = requests.get("https://api.example.com/users")
#     response.raise_for_status()
#     data = response.json()
# for user in data:
#     print(user.get("name"))
# except requests.exceptions.requestException  as e :
#     print("an error occurred : ", e)
# except valueError as e :
#     print("Value error occurred : ", e)
# except KeyError as e :
#     print("Key error occurred : ", e) 


    # ------------------

# def find_duplicates(lst):
#     known= set()
#     duplicates = set()
#     for i in lst:
#         if i in known:
#             duplicates.add(i)
#         known.add(i)
#     return duplicates

# print(find_duplicates([1, 2, 3, 2, 4, 3]))  

# /---------------

# my_tuple = [1, 2, 3]
# my_tuple[2] = 10
# print(my_tuple)

# ---

