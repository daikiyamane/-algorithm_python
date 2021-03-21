def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_num = 2000000000
    min_num2 = 2000000000

    for i in range(n):
        if min_num2 > a[i]:
            min_num2 = a[i]
        if min_num > min_num2:
            # 最小値の二番目を渡す
            min_num2 = min_num
            min_num = a[i]
    print(min_num2)


main()
