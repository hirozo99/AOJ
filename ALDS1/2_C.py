def swap(a, i ,j):
    k = a[j]
    a[j] = a[i]
    a[i] = k

def selectionsort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        swap(a, i, minj)

def bubblesort(a, n):
    flag = 1
    while flag:
        flag = 0
        for j in range(n-1, 0, -1):
            if a[j][1] < a[j-1][1]:
                swap(a, j-1, j)
                flag = 1

# 入力
n = int(input())
a = list(input().split())
b = a
# 出力
bubblesort(a, n)
print(" ".join(a))
print("Stable")
selectionsort(b, n)
print(" ".join(b))
if a == b:
    print("Stable")
else:
    print("Not stable")
