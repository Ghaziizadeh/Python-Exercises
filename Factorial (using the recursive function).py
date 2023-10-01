def factorial(num):
    # بررسی شرط خاتمه
    if num == 1:
        return 1
    # بازگشتی
    out = num * factorial(num - 1)
    return out

num = int(input("Please enter number: "))
out = factorial(num)
print(out)