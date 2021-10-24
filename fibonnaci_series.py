c = int(input("Till term:"))
a = 0
b = 1
print(a,b,"",sep=",",end="")
for i in range(c-2):
     d = a+b
     a = b
     b = d
     print(d,end=",")
     
