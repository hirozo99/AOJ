N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    minj = i
    for j in range(i, N):
        if A[j] < A[minj]:
            minj = j
    if i != minj:
        ans += 1
    A[i], A[minj] = A[minj], A[i]

print(*A)
print(ans)