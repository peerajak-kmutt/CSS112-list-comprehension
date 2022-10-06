def p4():
   posneg = [ int(i) for i in input().split()]
   noneg = [i for i in posneg if i<0]
   ans = len(noneg)
   print(ans)
