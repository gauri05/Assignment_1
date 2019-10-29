# stars
def print_stars(val):
    ans = 0
    while ans < val:
        print("*")
        ans = ans + 1


print("Enter the number::::")
num = input()
print_stars(int(num))
