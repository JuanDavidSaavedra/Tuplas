A = (1,"Suarez","Roney",25)
B = (2, "Suarez", "A", 35)
C = (3, "Suarez", "B", 30)
D = (4, "Suarez", "C", 25)
E = (5, "Suarez", "D", 41)
F = (6, "Suarez", "E", 39)
G = (7, "Suarez", "F", 48)

v=[]

v.append(A[3])
v.append(B[3])
v.append(C[3])
v.append(D[3])
v.append(E[3])
v.append(F[3])
v.append(G[3])

acu = 0
for i in range(7):
    acu = acu + v[i]
pro = acu/7

c = 0
for i in range(7):
    if v[i]>pro:
        c = c+1
print(pro)
print(c)



