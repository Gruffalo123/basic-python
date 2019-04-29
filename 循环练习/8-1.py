# 拓展：请输出1-2+3...-99除88以外的和（88之后奇偶正负对调）
i = 1
j = 1
sum = 0
while i <= 99:
    if i == 88:
        i = i + 1
        continue
    if i%2 == 1:
        sum = sum + i*j
    else:
        sum = sum + i*j
    j = -j
    i = i + 1
print(sum)