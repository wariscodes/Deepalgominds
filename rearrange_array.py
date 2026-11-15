arr = [3, 1, -2, -5, 2, -4]

pos = []
neg = []

for num in arr:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

ans = []

for i in range(len(pos)):
    ans.append(pos[i])
    ans.append(neg[i])

print(ans)
