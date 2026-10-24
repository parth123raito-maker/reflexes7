# 
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# 
# 
# n = int(input("Enter a number: "))
# i = 1
# 
# while i <= 10:
#     print("the table of n is=", i * n)
#     i += 1
# 
# 
# n = int(input("enter a number: "))
# i = 1
# while i <= 10:
#     print("soln is=", i ** n)
#     i += 1
# 
# 
# Search for a number x in this tuple using a loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
# x = 36
# idx = 0
# while idx < len(nums):
#     if nums[idx] == x:  
#      print("found it=", idx)
#      break
#     idx += 1
# print("end code")
# 
# nums = (1, 4, 9, 16, 100, 906, 49, 64, 81, "a", 89)
# x = 1
# idx = 0
# while idx < len(nums):
#     if nums[idx] == x:
#         print("gotta=", idx)
#         break
#         idx += 1
# 
# i = 0
# while i <= 99:
#     i  += 1
#     if i % 5 == 0:
#         continue
#     print(i)
# 
# nums = [1, 2, 3]
# for el in nums:
#   if el == 2:
#     break
# print(el)
# 
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for num in nums:
#     if num == 9:
#         break
# print(num)
# 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49
# idx = 0
# for num in nums:
#  if num == x:
#    print("Found at index", idx)
#  break
# idx += 1
# 
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# idx = 0
# for num in nums:
#     if num == 64:
#         print("found:", idx)
#         break
#     idx += 1
# 
# for el in range(9,12,2):
#     print(el)
# 
# for i in range(100, 0, -1): 
#  print(i)
# 
# n = int(input("enter number: "))
# for el in range(1,1001):
#  print(el,el * n)
# 
# n = int(input("enter number: "))
# i = 0
# while  i <= 10:
#     print("sum is=", i * (n*(n+1)/2) )
#     i += 2
# 
# Q2. Find the factorial of n (using for).
# n = int(input("Enter n: "))
# fact = 1 
# for i in range(1, n + 1):
#  fact *= i
# print("Factorial =", fact)
# 

