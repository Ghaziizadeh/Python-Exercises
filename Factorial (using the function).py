def factorial(num):
    if num < 0:
        return False
    output = 1
    for i in range(2, num + 1):
        output *= i
    return output


num = int(input("Please enter number: "))
out = factorial(num)
print(out)
