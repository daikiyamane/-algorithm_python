def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    exist = False

    for i in range(2**n):
        sum = 0
        print("pattern={}:".format(i), end="")
        for j in range(n):
            if ((i >> j) & 1):
                sum += a[j]
        print(sum)
        if sum == w:
            exist = True
            break
    if exist:
        print("Yes")
    else:
        print("No")


main()
