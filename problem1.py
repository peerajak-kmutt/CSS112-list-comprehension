def p1():
    x=input().split()
    c=input()
    ans = [i.count(c) for i in x]
    print(*ans)


