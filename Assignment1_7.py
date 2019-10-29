def checknum(val):
    ans = val %5
    if ans == 0:
        print("True")
    else:
        print("False")
print("Check Number is divided by 5")
print("Enter number::::")
num=input()
checknum(int(num))