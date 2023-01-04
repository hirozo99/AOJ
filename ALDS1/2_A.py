N = int(input())
A = list(map(int, input().split()))

flag = 0
for i in range(N):
    for j in range(N-1):
        if A[j+1] < A[j]:
            A[j], A[j+1] = A[j+1], A[j]
            flag += 1

print(*A)
print(flag)