def reverse(n):
    print(n[::-1])
a=[]
n=int(input("enter numbeer of elements you want to enter:"))
for i in range(n):
    e=int(input("enter elemen:"))
    a.append(e)
reverse(a)