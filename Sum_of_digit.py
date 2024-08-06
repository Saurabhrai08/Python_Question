num = 1234
sum=0

def findsum(num,sum):
    if num == 0:
        return sum
    

    digit = int(num%10)
    sum +=digit
    num = num / 10
    return findsum(num, sum)

result = findsum(num, sum)

print (result)

    