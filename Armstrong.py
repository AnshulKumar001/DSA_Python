num = int(input("Enter a number: "))
n = num

# Count digits
count = 0
temp = num
while temp > 0:
    count += 1
    temp = temp // 10

# Armstrong calculation
result = 0
temp = num
while temp > 0:
    id = temp % 10
    result = result + (id ** count)
    temp = temp // 10

# Final check
if n == result:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
