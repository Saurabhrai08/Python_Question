numbers = [4,7,1,8,3]

def Largest_Number(num):
   largest = numbers[0]  # Initialize the largest number with the first element
   for num in numbers:
        if num > largest:
            largest = num
   return largest



result = Largest_Number(numbers)
print (result)
