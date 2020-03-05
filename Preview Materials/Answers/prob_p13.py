a=int(input())
b=int(input())
p=int(input())

c=complex(a,b)
z=c**p
r=z.real
i=z.imag

r=int(r)
i=int(i)

print(r)
print(i)