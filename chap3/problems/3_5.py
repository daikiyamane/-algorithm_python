def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_v = 2000000000
    for i in range(n):
        pv = calc(a[i])
        if min_v > pv:
            min_v = pv
    print(min_v)


def calc(n):
    c = 0
    while True:
        if n % 2 == 0:
            n = n // 2
            c += 1
        else:
            break
    return c


main()
