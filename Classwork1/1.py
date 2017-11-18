q = 1
x = 1
e = 1
n =int(input())
k = int(input())
for i in range(1,n+1):
    q = q*i
for i in range(1,k+1):
    x = x*i
for i in range(1,n-k+1):
    e = e*i
print(q/(x*e))
