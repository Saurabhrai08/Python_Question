num = 3
limit = 20

def multiples(num,limit):
    for i in range (num ,limit + 1 , num):
        print (i, end = ",")

result = multiples(num , limit)