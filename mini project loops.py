# #different loops
# print("There are 4 different types of series:")
# print("1) 1,2,3,4,5,6,7...n")
# print("2) 1,2,4,8,16...n (Series is 2 raised to n)")
# print("3) -100,-96,-92...n (Numbers differ by 4)")
# print("4) 1,10,100,1000...n (Series is 10 raised to n)")
# print("5) Exit")
# print()
# loop=1
# while loop==1:
    
#     choice=int(input("Enter your choice (1,2,3,4,0): "))
    
#     if choice==1:
#         n=int(input("Enter a number: "))
#         for i in range(1,n):
#             print(i,end=",")
#         print(i+1)
#         print()
#     elif choice==2:
#         n=int(input("Enter a number: "))
#         for i in range(0,n):
#             print(2**i, end=",")
#         print(2**(i+1))
#         print()
#     elif choice==3:
#         n=int(input("Enter a number: "))
#         if n%4==0:
#             for i in range(-100,n,4):
#                 print(i,end=",")
#             print(i+4)
#             print()
#         else:
#             if n>0:
#                 r=n-(n%4)
#                 for i in range(-100,r,4):
#                     print(i,end=",")
#                 print(r)
#                 print()
#             else:
#                 r=n-(n%4)
#                 for i in range(-100,r,4):
#                     print(i,end=",")
#                 print(i+4)
#                 print()
#     elif choice==4:
#         n=int(input("Enter a number: "))
#         for i in range(1,n):
#             print(10**i,end=",")
#         print(10**(i+1))
#         print()
    
#     elif choice==0:
#         loop=0
#         print("Ok, good bye!")
#     else:
#         loop=0
#         print("Invalid input, try again later.")
        
# sum=0
# for i in range(2,20,3):
#     sum+=i
#     print(i,sum)

#1
# n=int(input("Enter a number: "))
# sum=0
# if n%2==0:
#     for i in range(2,n,2):
#         sum+=i
#         print(i,end=",")
#     print(i+2)
#     print("Sum =",sum+i+2)
# elif n%2!=0:                    
#     for i in range(2,n-1,2): #range(2,19,2)
#         sum+=i
#         print(i,end=",")
#     print(i+2)
#     print("Sum =",sum+i+2)

#2
# n=int(input("Enter a number: "))
# sum=0
# if n%10==0:
#     for i in range(10,n-1,10):
#         sum+=i
#         print(i,end=",")
#     print(i+10)
#     print("Sum =",sum+i+10)
# elif n%10!=0:
#     for i in range(10,n-(n%10),10):
#         sum+=i
#         print(i,end=",")
#     print(i+10)
#     print("Sum =",sum+i+10)

#3
n=int(input("Enter a number: "))
sum=0
i=4
if n%4==0:
    while i<n:
        sum+=i
        print(i,end=",")
        i+=4
    print(i)
    print("Sum =",sum+i)
elif n%4!=0:
    while i<n-(n%4):
        sum+=i
        print(i,end=",")
        i+=4
    print(i)
    print("Sum =",sum+i)