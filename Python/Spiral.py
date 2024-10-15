def dodawanie_rzedu(rzad):
    macierz = []
    for i in range(rzad):
        macierz.append(input().split())
    return macierz

n = int(input())
a = 0
b = 0
wyraz = []
macierz = dodawanie_rzedu(n)
b = b - 1

for el in range(n):
    b = b + 1
    wyraz.append(macierz[a][b])
    
n = n - 1

while n>0:
    
    for el in range (n):
        a = a + 1
        wyraz.append(macierz[a][b])
    for el in range (n):
        b = b - 1
        wyraz.append(macierz[a][b])
        
    n = n - 1
    
    for el in range (n):
        a = a - 1
        wyraz.append(macierz[a][b])
    for el in range (n):
        b = b + 1
        wyraz.append(macierz[a][b])
    
    n = n - 1
    
    
print(" ".join(list(map(str, wyraz))))