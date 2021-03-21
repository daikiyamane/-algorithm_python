def main():
    n, v = map(int, input().split())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if a[i] == v:
            c += 1
    print(c)


main()
