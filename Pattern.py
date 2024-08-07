n = 4

for i in range (n):
    for j in range (i + 1):
        print("*",end = " ")
    print()

print ("--------------------------------------")


for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)


print("------------------------------------")

for i in range(1, n + 1):
    print("  " * (i - 1), end="") 
    for j in range(1, n - i + 2):
        print("* ", end="")  

    print()