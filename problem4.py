def p4():
   posneg = [ int(i) for i in input().split()]
   numneg = [i for i in posneg if i<0]
   ans = len(numneg)
   print(ans)
