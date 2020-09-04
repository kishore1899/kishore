a=list(map(int,input().split(" ")))
a.sort()
for i in range(0,len(a)):
    if i+1!=a[i]:
        print(i+1)
        break;