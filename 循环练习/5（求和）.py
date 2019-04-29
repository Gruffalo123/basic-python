# 5、求1-2+3-4+5 ... 99的所有数的和
i = 1
sum = 0
while i < 100:
    if i%2 == 0:
        sum -= i
    else:
        sum += i
    i += 1
print(sum)