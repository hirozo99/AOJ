n = int(input())

mn = float("inf")
ans = -float("inf")
for _ in range(n):
    r = int(input())
    ans = max(ans, r-mn)
    mn = min(mn, r)
print(ans)
