def main():
    n, v = map(int, input().split())
    a = list(map(int, input().split()))
    found_id = -1
    for i in range(n):
        if a[i] == v:
            found_id = i
            break
    print(found_id)


main()
