def p6():
  xi =  [ int(i) for i in input().split()]
  yi =  [ int(i) for i in input().split()]
  zi = [xi[i]*yi[i] for i in range(len(xi))]
  print(*zi)
