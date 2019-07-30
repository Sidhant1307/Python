print ('\n','1.Add','\n','2.Subtract','\n','3.Multiply','\n','4.Divide','\n','5.SimpleInterest')
choice =int(input('Enter choice = '))
if (choice==1):
    a = int(input('Enter 1st No. = ' ))
    b = int(input("Enter 2nd No. = "))
    sum = a+b
    print('Sum = ',sum)
elif(choice==2):
    a = int(input('Enter 1st No. = ' ))
    b = int(input("Enter 2nd No. = "))
    sub = a-b
    print ('Subtract = ',sub)
elif(choice==3):
    a = int(input('Enter 1st No. = ' ))
    b = int(input("Enter 2nd No. = "))
    mul = a*b
    print ('Multiply = ',mul)
elif(choice==4):
    a = int(input('Enter 1st No. = ' ))
    b = int(input("Enter 2nd No. = "))
    div = a/b
    mod = a%b
    print ('Divide = ',(div),'\n','Remainder =',(mod))
elif(choice==5):
    p = int(input("Enter principal amount :"))
    r = int(input("Rate of interest: "))
    t = int(input('Time duration : '))
    SI = (p*r*t)/100
    print ('Simple Interest =',SI)
else:
    print('incorrect choice')
