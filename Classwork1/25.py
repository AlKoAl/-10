n = int(input())
i = -1
j = 0
max_j = n - 1
max_i = n - 1
min_j = 1
min_i = 0
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]
while True:
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    if j == (n - 1) // 2 and i == n // 2:
        break
print()
for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end='\t')
    print()
input()