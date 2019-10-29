def first_ten_even_num(val):
    num = val * 2
    ans= list(range(1,num+1))
    print(ans)

    for i in range(len(ans)):
        if ans[i] % 2 == 0:
            print(ans[i], end="  ")
print("Enter Number::::")
num=input();
first_ten_even_num(int(num))