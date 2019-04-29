# 请输出1-2+3...+99除88以外的和
i = 1
sum = 0
while i <= 99:
    if i == 88:
        i = i + 1
        continue
    else:
        if i%2 == 1:
            sum = sum + i
        else:
            sum = sum - i
    i = i + 1
print(sum)