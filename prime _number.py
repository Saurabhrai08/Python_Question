n = int (input( " Enter the No:"))

if n<=1:
    print("not prime number")

else:
    for i in range (2,n):
        if (n % i == 0):
            print(" Not a prime Number" )
            break
        

    else:
        print(" Prime Number")
        

print("-------------------------------------------")

flag = True

for i in range (2,n):
        
        if (n % i == 0):
             flag = False
             break

if(flag):
     print("number is prime ")

else:
     print("Not a Prime Number")