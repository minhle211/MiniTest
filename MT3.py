#Phan 1
#bai 1
# def chanle(a):
#     return (a%2==0)
# a = int(input("Input a number: "))
# if(chanle(a)):
#     print("This number is even")
# else:
#     print("This number is not even")

#bai2
# def area(a):
#     return a*a*3.14
# a = int(input("Input a number: "))
# print(f"Circle's area: {area(a)}")

#bai 3
# def re_str(a):
#     b = ""
#     for i in range(0,len(a)):
#         b = a[i] + b
#     return b
# a = input("Input a text: ")
# print(f"Reversed text: {re_str(a)}")

#bai 4
# def re_str(a):
#     b = ""
#     for i in range(0,len(a)):
#         b = a[i] + b
#     return b
# def if_palin(a):
#     if(re_str(a)==a):
#         print("This is a palindrome.")
#     else: print("This is not a palindrome.")
# a = input("Input a text: ")
# if_palin(a)


#Phan 2
#bai 1
# def gt(a):
#     d = 1
#     for i in range(1,a+1):
#         d*=i
#     return d
# a = int(input("Input a number: "))
# print(f"{a}! = {gt(a)}")

#bai 2
# def sort(a):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if(a[i]<a[j]):
#                 temp=a[i]
#                 a[i]=a[j]
#                 a[j]=temp
# A = [5,1,8,92,-1,30]
# print("Original list: ")
# print(A)
# sort(A)
# print("Sorted list: ")
# print(A)

#bai 3
# def fibo(a):
#     i=2
#     a1=a2=1
#     if(i==1):
#         print(a1)
#     else:
#         print(f"{a1} {a2}",end=' ')
#     while(i<a):
#         an=a1+a2
#         print(an,end=' ')
#         a1=a2
#         a2=an
#         i+=1
# a = int(input("Input a number: "))
# fibo(a)


#bai 1 codelearn
def khoitao(B):
    for i in range(26):
        B.append(int(i+1))
def highest(a):
    B=[]
    khoitao(B)
    max=0
    str=""
    maxstr=""
    i=0
    sume=0
    for i in a:
        if(i!=' '):
            sume+=B[int(ord(i)-ord('a'))]
            str=str+i
        d=a[len(a)-1]
        if(i==' ' or i==d):
            if(sume>max):
                max=sume
                maxstr=str
            str=""
            sume=0
    return maxstr
str = input("Input a string: ")
print(f"Highest scoring word is: {highest(str)}")