def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_n = 200000000
    max_n = -1
    for i in range(n):
        if a[i] <= min_n:
            min_n = a[i]
        if max_n <= min_n:
            max_n = a[i]
    print(max_n-min_n)


main()
