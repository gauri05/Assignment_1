import array as arr
val = list(range(1,11))
print(val)
ret=arr.array('i',val)

ret.reverse()
for j in range(len(ret)):
    print(ret[j], end ="   ")