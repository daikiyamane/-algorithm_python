def main():
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    for v in a:
        if n == v:
            flag = True

    if flag:
        print("Yes")
    else:
        print("No")


main()
