def main():
    S = str(input())
    N = len(S)

    ans = 0

    for bit in range(1 << (N-1)):
        A = ''
        for i in range(N):
            A += S[i]
            if bit & (1 << i):
                A += '+'
        print(A)
        A = A.split('+')
        for a in A:
            if a:
                ans += int(a)

    print(ans)
    return


if __name__ == '__main__':
    main()
