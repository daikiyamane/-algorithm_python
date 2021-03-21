def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_num = 20000000000
    for i in range(n):
        for j in range(n):
            # 和がk未満は捨てる
            if k > a[i] + b[i]:
                continue
            if a[i] + b[i] <= min_num:
                min_num = a[i] + b[i]
    print(min_num)


main()
