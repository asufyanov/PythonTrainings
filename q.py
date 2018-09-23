n = int(input())
a = list(map(int, input().split()))



for i in range(0, n-1):

    if i % 2 == 0:

        a[i], a[i+1] = a[i+1], a[i]


print(a)