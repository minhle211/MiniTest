# from pickle import FALSE, TRUE
# from turtle import *
#Phan 1
# color = ['red','blue','teal','green','orange']
# print("Color list: ")
# print(color[0],end='')
# for i in range(1,len(color)):
#     print(f", {color[i]}",end='')
# print("")
# str = input("Input a new color: ")
# color.append(str)
# print(color[0],end='')
# for i in range(1,len(color)):
#     print(f", {color[i]}",end='')


#Phan 2
#bai1
# pos = int(input("Input position: "))
# print(f"Color at position {pos}: {color[pos-1]}")

#Bai 2
# pos = input("Item to delete: ")
# if(pos>='0' and pos<='9'):
#     del color[int(pos)-1]
# else: color.remove(pos)
# print(color[0],end='')
# for i in range(1,len(color)):
#     print(f", {color[i]}",end='')

#Bai 3
# penup()
# goto(-100,0)
# pendown()
# for i in range(len(color)):
#     pencolor(color[i])
#     forward(50)
#     penup()
#     forward(20)
#     pendown()

#Phan 3
#A = [1,5,-20,9,333]
#Bai 1
# num = int(input("Input a number: "))
# check = FALSE
# POS=0
# for i in range(len(A)):
#     if(num==A[i]):
#         check=TRUE
#         POS=i
#         break
# if(check==TRUE):
#     print("Number found at position ",POS+1)
# else: print("Number not found")
#Bai 2
# d=0
# for i in range(len(A)):
#     d+=A[i]
# print("Sum of all numbers: ",d)
#Bai 3
# B = []
# print("Input the list of numbers")
# d = 10
# z=0
# print("Enter 0 to finish.")
# while d!=0:
#     d=int(input())
#     B.append(d)
#     z+=d
# print("Sum of numbers in list: ",z)

#Phan 4
#Bai 1
# A= [5,1,2,6,8,20,40,30]
# print("Even numbers: ",end='')
# for i in range(len(A)):
#     if(A[i]%2==0):
#         print(A[i],end=' ')

#Bai2
# B = []
# print("Input the list of numbers")
# print("Enter 0 to finish.")
# d=10
# while d!=0:
#     d=int(input())
#     if(d==0):
#         break
#     B.append(d)
# print("Even numbers in list: ",end='')
# for i in range(len(B)):
#     if(B[i]%2==0):
#         print(B[i],end=' ')


#Phan 5
# dis = ["BĐ","BTL","CG","ĐĐ","HBT"]
# pop = [247100,333300,266800,420900,318000]
#Bai 1
# print("Indices of: ")
# a=0 
# b=0
# for i in range(len(pop)):
#     if(pop[a]>pop[i]):
#         a=i
#     if(pop[b]<pop[i]):
#         b=i
# print("- Most populated dist.: ",b)
# print("- Least populated dist.: ",a)

#Bai 2
# print("Names of: ")
# print("- Most populated dist: ",dis[b])
# print("- Least populated dist: ",dis[a])


#Phan 6
# area = [9.224,43.35,12.04,9.96,10.09]

# Den = []
# for i in range(len(area)):
#     Den.append(pop[i]/area[i])
# print("Population density of: ")
# for i in range(len(Den)):
#     print(f"- {dis[i]}: {Den[i]}")

# print("Average population density : ")
# d=float(0)
# for i in range(len(Den)):
#     d+=Den[i]
# z=len(Den)
# d/=float(z)
# print(d)


#Phan 7
# score= [78,56,67,45,70]
#Bai 1
# print("High scores: ")
# for i in range(len(score)):
#     print(f"{i+1}. {score[i]}")

#Bai 2
# d = int(input("Input new score: "))
# score.append(d)
# for i in range(len(score)):
#     print(f"{i+1}. {score[i]}")

#Phan 8
# d = int(input("Input new score: "))
# score.append(d)
# for i in range(len(score)):
#     for j in range(len(score)):
#         if score[i]>score[j]:
#             temp=score[i]
#             score[i]=score[j]
#             score[j]=temp
# for i in range(len(score)):
#     print(f"{i+1}. {score[i]}")

# d = int(input("Input new score: "))
# score.append(d)
# for i in range(len(score)):
#     for j in range(len(score)):
#         if score[i]>score[j]:
#             temp=score[i]
#             score[i]=score[j]
#             score[j]=temp
# for i in range(5):
#     print(f"{i+1}. {score[i]}")