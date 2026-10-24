# # a = 10
# # b = 5
# # sum = a + b
# # print(sum)
# 000 
# # print(a == b)
# # # print(a ** b)
# # # print(a % b)
# # # print(a // b)
# 000
# # # num = 50
# # # num += 60
# # # print(num)
# # # print(not (a == b))
# # # print(not (a >= b) and (b < a))
# 000
# # a = 20
# # b = "30"
# # c = int(b)
# # sum = a + c
# # print(sum)
# 000
# # price = int(input("Enter the price: "))
# # print("price after 50% tax is", price * 1.1)
# 000
# # a = int(input("Enter the value of a: "))
# # b = int(input("Enter the value of b: "))
# # print("a is greater than b", a >= b)
# 000
# # a = "AVENGERS"
# # # print(a[5:7])
# 000
# # a = input("Enter your name: ")
# # print("length:", len(a))
# 000
# # a = "BATMAN"
# # print(a.endswith("AN"))
# 000
# # n = input("Enter the name:")
# # print("IT ENDS", n.endswith("CHU"))
# 000
# # light = "green"
# # if light == "yellow":
# #     print("look")
# # elif light == "red":
# #     print("stop")
# # elif light == "pink":
# #     print("go")
# # else:
# #     print("go")
# 000
# #     marks = int(input("Enter marks (0-100): "))
# #     if not 0 <= marks <= 100:
# #         print("Please enter a mark from 0 to 100.")
# #     elif marks >= 90:
# #         grade = "A"
# #     elif marks >= 80:
# #         grade = "B"
# #     elif marks >= 70:
# #         grade = "C"
# #     else:
# #         grade = "D"
# #
# #     if 0 <= marks <= 100:
# #         print("Grade:", grade)
# # except ValueError:
# #     print("Please enter a number only, such as 72.")
# 000
# # num = int(input("Enter a number: "))
# # if num % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")
# 000
# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))
# # c = int(input("Enter third number: "))
# # if a >= b and a >= c:
# #     print("a is greatest")
# # elif b >= c:
# #     print("b is greatest")
# # else:
# #     print("c is greatest")
# 000
# # a = int(input("enter the number: "))
# # if a % 7 == 0:
# #     print("number is divisible by 7")
# # else:
#     # print("number is not divisible by 7")
#  # import math
# # x = int(input("enter the value of x: "))
# # y = int(input("enter the value of y:"))
# # print("the distance is =", math.sqrt(x ** 2 + y ** 2)
# 000
# # import math
# # x = float(input("enter the value of x: "))
# # print(math.sqrt(x))
# # print(math.ceil(x))
# # print(math.floor(x))
# # print(math.pow(x))
# 000
# # import math
# # print("value of tau =", math.tau)
# # print("value of e =", math.e)
# # print("value of NaN =", math.nan)
# # print("value of pi =", math.pi)
# 000
# # import math
# # x = -89
# # print(math.fabs(x))
# 000
# # import math
# # force = int(input("Enter force: "))
# # angle = int(input("Enter angle: "))
# # print("vertical component =", force * math.sin(math.radians(angle)))
# 000
# # import random

# # # a = random.randint(5,10)
# # # a = random.randrange(7,15)
# # a = random.random()
# # print(a)
# 000
# # import random

# # sensor_value = random.randint(10,50)

# # print(sensor_value)
# 000  
# # import math
# # angle = float(input("Enter the angle in degrees: "))
# # print("sin of angle is =", math.sin(math.radians(angle)))
# 000
# # a = 0b1110
# # b = 0b1010
# # c = a & b
# # print(bin(c))
# # d = a ^ b
# # print(bin(d))
# # 000
# # import math
# # angle = int(input("enter the angle: "))
# # print(math.sin(math.radians(angle)))
# 000
# # import math
# # x = int(input("enter the number: "))
# # # if x % 3 == 0:
# # #    print("x is divisible by 3")
# # # elif x % 5 == 0:
# # #    print("x is divisible by 5")
# # if x % 3 == 0 and x % 5 == 0:
# #    print("x is divisible by both")
# # else:
# #    print("not divisible")
# 000
# movies = []

# 000
# # h1 = int(input("Enter 1st hours: "))
# # m1 = int(input("Enter 1st minutes: "))
# # s1 = int(input("Enter 1st seconds: "))

# # h2 = int(input("Enter 2nd hours: "))
# # m2 = int(input("Enter 2nd minutes: "))
# # s2 = int(input("Enter 2nd seconds: "))

# # Convert both times to minutes, then find the absolute difference.
# # t1 = h1 * 60 + m1 + s1 / 60
# # t2 = h2 * 60 + m2 + s2 / 60

# # time_diff = abs(t2 - t1)
# # print("Time difference in minutes =", time_diff)
# 000
# # text = "hello programming"
# # text = text.replace("hello", "hi")
# # print(text[0])
# # print(text[-1])
# # print(text[0:6])
# # print(text.capitalize())
# # print(text.count("m"))
# # print(text.find("programming"))
# 000
# student = {
#     "name": "parth",
#     "age": 34,
#     "marks": {
#         "phy": 23,
#         "chem": 34,
#         "math": 34,
#     }
# }
# print(student["marks"])
# print(student["marks"]["chem"])
# print(student["age"])
# student["name"] = "naav"
# print(student)
# print(student.keys())
# print(student.values())
# print(student.get("name"))
# 000
# nums = {1, 2, 3}
# nums.add(4)
# nums.add(2) 
# print(nums)
# nums.remove(3)
# print(nums)
# nums.clear()
# print(nums)
# 000
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.union(set2))
# print(set1.intersection(set2))
# 000
# set1 = {9}
# set2 = {"9.0"}
# print(set1.union(set2))
# 000
# subjects = {"python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"}
# print("Classrooms needed:", len(subjects))
# 
# 000
# movies = []

# movies.append(input("Enter first movie: "))
# movies.append(input("Enter second movie: "))
# movies.append(input("Enter third movie: "))

# print(movies)
# 000

# import math
# print(math.sin((math.pi/6)))
# 000

END CODE