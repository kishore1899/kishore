a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
 
    c+=list(str(i)).count("1")
print(c)