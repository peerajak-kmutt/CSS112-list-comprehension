def p2():
    inlist = input().split()
    outlist = [i for i in inlist if i>=0]
    print(" ".join(outlist))
