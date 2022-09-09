from turtle import *
import turtle
import math
# #bai 1
# first = input("First name:")
# last = input("Last name:")
# print(f"Your full name is {first} {last}")

#bai2
# Input = input("Your Input:")
# print("Capitalized: ",end='')
# for i in Input:
#     print(i.capitalize(),end='')

#bai3
# d = int(input("Input a number: "))
# z = d*d
# print(f"Squared input: {float(z)}")

#bai4
# z = int(input("Input circle's radius: "))
# t= turtle.Turtle()
# t.circle(z)



#Phan2
#Bai1
# for i in range(3,13):
#     print(i,end=' ')

#Bai2
# d = int(input("Input a number: "))
# if(d<0):
#     print("Please try again!")
# else: 
#     for i in range(d+1):
#         print(i,end=' ')

#bai3
# n = int(input("Input a number: "))
# for i in range(n):
#     if(i%2==1):
#         print(i,end=' ')

#Bai 4
# t=turtle.Turtle()
# n=int(input("Input number of edges: "))
# for i in range(n):
#     turtle.forward(50)
#     turtle.right(360/n)

#Phan3
#Bai1
# n = int(input("Input a number: "))
# if(n>13):
#     print("This number is larger than 13")
# elif n==13:
#     print("This number is equal to 13")
# else: print("This number is not larger than 13")


#Bai2
# n = int(input("Input a number: "))
# if(n%2==0):
#     print("This number is even")
# else: print("This number is not even")

#Bai 3
# n = int(input("Input a month: "))
# if(n>12 or n<1):
#     print("Invalid")
# elif(n==4 or n==6 or n==9 or n==11):
#     print("This month has 30 days")
# elif(n==2):
#     print("This month has 28 days")
# else: print("This month has 31 days")

#Phan4
#bai1
# print("== Registration ==")
# User = input("Username: ")
# Pass = input("Password: ")
# Email = input("Email: ")
# print("Registered successfully.")

#bai2
# print("== Registration ==")
# print(" ")
# User = input("Username: ")
# print(" ")
# Pass = input("Password: ")
# repeat = input("Repeat password: ")
# while(repeat!=Pass):
#     print("Passwords not match. Please input again")
#     repeat = input("Repeat password: ")
# print(" ")
# Email = input("Email: ")
# print(" ")
# print("Registered successfully.")

#bai3
# print("== Registration ==")
# print(" ")
# User = input("Username: ")
# print(" ")
# word = False
# num = False
# while (word!=True and num!=True):
#     Pass = input("Password: ")
#     for i in Pass:
#         if(i>='a' and i<='z'):
#             word=True
#         if(i>='0' and i<='9'):
#             num=True
#     if(word==True and num==True and len(Pass)>=8):
#         repeat = input("Repeat password: ")
#         while(repeat!=Pass):
#             print("Passwords not match. Please input again")
#             repeat = input("Repeat password: ")
#         break
#     else: 
#         print("Invalid password. Please input again")
#         word=False
#         num=False
# print(" ")
# atsite=False
# stop=False
# while (atsite!=True and stop!=True):
#     Email = input("Email: ")
#     for i in Email:
#         if(i=='@'):
#             atsite=True
#         if(i=='.'):
#             stop=True
#     if(atsite==True and stop==True):
#         print(" ")
#         print("Registered successfully.")
#         break
#     else: 
#         print("Invalid email. Please input again")
#         atsite=False
#         stop=False

#Phan 5
# a=0
# b=0
# c=0
# while(a==0 and b==0):
#     a = float(input("Input a: "))
#     b = float(input("Input b: "))
#     c = float(input("Input c: "))
#     if(a==0 and b==0):
#         print("Moi nhap lai")
# delta = float(b*b-4*a*c)
# if(delta==0):
#     print(f"Solution: {-b/(2*a)} ")
# elif delta>0:
#     sol1 = float((-b+math.sqrt(delta)))/(2*a)
#     sol2= float((-b-math.sqrt(delta))/(2*a))
#     print(f"Solution 1 : {sol1}")
#     print(f"Solution 2 : {sol2}")
# else: print("No value")

#bai2
# x = input("Input a number:")
# d=1
# z=0
# for i in x:
#     if(d%2==0):
#         z=z+int(i)
#     d+=1
# print(f"Sum of the even digit in the number: {z}")