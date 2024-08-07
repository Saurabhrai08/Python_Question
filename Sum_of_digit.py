num = 12345
sum=0

def findsum(num,sum):
    if num == 0:
        return sum
    

    digit = int(num%10)
    sum +=digit
    num = num / 10
    return findsum(num, sum)

result = findsum(num, sum)

print ("The sum of digit :",result)

print("-----------------------------------------")

while(num>0):
    unit_digit = num% 10 
    sum += unit_digit
    num = num//10

print("The sum of digit :",sum)
