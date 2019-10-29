def even_odd(val):
    ans =val % 2
    if ans == 0:
        print("Even number")
    else:
        print("Odd number")

print("Enter number")
val=input();
even_odd(int(val))

