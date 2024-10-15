s = input()
print(all([(int(s)%i) for i in range(2,int(int(s)**(1/2))+1)]) and int(s) > 1)