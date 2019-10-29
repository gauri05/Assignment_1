def Add(val1, val2):
    ans = val1 + val2
    return ans


print("Enter first number:")
val1 = input()
print("Enter second number:")
val2 = input()
ret = Add(int(val1), int(val2))
print("Addition of 2 number is:", ret)
