def funkcja_palindrom(tekst):
    return tekst == tekst[::-1]

def wynik():
    tekst = input().lower()
    if funkcja_palindrom(tekst):
        return True
    if len(tekst) == 2:
        return True
    for i in range(len(tekst)):
        palindrom = tekst[:i] + tekst[i + 1:]
        if funkcja_palindrom(palindrom):
            return True
        for j in range(len(palindrom)):
            temp = palindrom[:j] + palindrom[j + 1:]
            if funkcja_palindrom(temp):
                return True
    return False

if __name__ == "__main__":
    if wynik()==True:
        print("YES")
    else:
        print("NO")


