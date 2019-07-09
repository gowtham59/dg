n1=int(input())
s2=list(map(int,input().split()))[:n1]
a3=s2.sort()
middleIndex =int( (len(s2))/2)
print(s2[middleIndex])
