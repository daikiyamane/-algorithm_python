def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_value = 200000000000
    for i in range(n):
        if min_value > a[i]:
            min_value = a[i]
    print(min_value)


main()
