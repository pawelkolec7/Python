n = int(input())
e = set(map(int, input().split()))
for el in e:
    if el+1 in e or el-1 in e:
        print("YES")
        break
else:
    print("NO")