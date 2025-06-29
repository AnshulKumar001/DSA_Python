num = int(input("Enter a number: "))
result = 0
n=num
while num > 0:
    digit = num % 10
    result = result * 10 + digit
    num = num // 10

if n == result:
    print("Number is  palindrome.")
else:
    print("Number is not palindrome.")





    
         