#import math
#1
# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# print(f"{a} + {b} = {a+b}")

#2
# a = int(input("Input a: "))
# b = int(input("Input b: "))
# c = int(input("Input c: "))
# delt = b*b - 4*a*c
# if(delt>0):
#     print("The equation has 2 solutions")
#     x1=(-b+math.sqrt(delt))/(2*a)
#     x2=(-b-math.sqrt(delt))/(2*a)
#     print(f"x = {x1} or x = {x2}")
# elif (delt==0):
#     print("The equation has 1 solution")
#     x=(-b+math.sqrt(delt))/(2*a)
#     print(f"x={x}")
# else: print("The equation has no solution")

#3
# str = input("Input a text: ")
# def palindrome(str):
#     return str == str[::-1]
# if(palindrome(str)==True):
#     print("This is a palindrome")
# else: print("This is not a palindrome")

#4
# print("== Welcome to MindX Restaurant ==")
# Con = True
# check = False
# A = []
# while(Con==True):
#     str = input("Please choose a dish: ")
#     for i in range(len(A)):
#         if(str==A[i]):
#             check=True
#     if(check==True):
#         print("You chose this already")
#     else:
#         print("Great choice!",end=' ')
#         A.append(str)
#         check=False
#     char = input("Anything else? (y/n):")
#     if(char == 'y'):
#         Con = True
#     else: Con = False
# print("Well done! Your order: ")
# for i in range(len(A)):
#     print(f"- {A[i]}")

#5
# Smartphone = {
#     'Iphone12' : 28000000,
#     'Samsung N10': 16000000,
#     'Oppo 93': 7500000,
#     'Vsmart': 7400000,
#     'Vivo': 4200000
# }
#     #Ct1
# str = input("Input name of phone: ")
# print(Smartphone.get(str))
#     #Ct2
# bud = int(input("Input your budget: "))
# print("Phone(s) that fit your budget: ")
# for i in Smartphone:
#     if(Smartphone[i]<=bud):
#         print(f"- {i}: {Smartphone[i]}")

#6
# a = int(input("Input a number: "))
# d = 0
# while int(a)>0:
#     d+=1
#     a/=10
# print(f"This number has {d} digit(s)")

#7
# A = [5,1,8,92,-1,30]
# print("Original list: ")
# print(A)
# for i in range(len(A)):
#     for j in range(len(A)):
#         if(A[i]<A[j]):
#             temp=A[i]
#             A[i]=A[j]
#             A[j]=temp
# print("Sorted list: ")
# print(A)

#8
# a = int(input("Input a number: "))
# a1 = a2 = 1
# print(f"First {a} Fibonacci number: ",end=' ')
# print(f"{a1} {a2} ",end='')
# for i in range(a-2):
#     an = a1+a2
#     a1=a2
#     a2=an
#     print(f"{an} ",end='')