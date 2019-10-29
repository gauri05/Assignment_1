def check(val1):
    if val1 == 0:
        print("Zero")
    elif val1 < 0:
        print("Negative")
    else:
        print("Positive")


print("Enter number:::")
val = input()
check(int(val))
