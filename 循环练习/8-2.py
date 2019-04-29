# 拓展：请输出1-2+3...-99除88以外的和（88之后奇偶正负对调）
# 以下是上一题的优化版：
i = 0
j = 1
sum = 0
while i < 99:
    i = i + 1
    if i == 88:
        continue
    else:
        sum = sum + i*j
        j = -j
print(sum)