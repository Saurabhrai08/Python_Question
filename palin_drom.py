str =  input ("Enter The message")
n = len(str)
revstr = ""
for i in range (n-1,-1,-1):
   revstr = revstr + str[i]
   

if (revstr == str):
   print("IT is palindrome")

else:
   print(" not a palindrome")
