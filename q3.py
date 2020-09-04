print("Enter x and y ")      
a=int(input())
b=int(input())
print("Before swapping")
print("x= "+str(a))
print("y= "+str(b))
a^=b
b^=a
a^=b
print("After swapping")
print("x= "+str(a))
print("y= "+str(b))