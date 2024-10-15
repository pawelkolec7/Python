n = int(input())
students = []
tests = []


for i in range(n):
    scores = []
    line = input().split()
    scores.append(line[0])
    
    for j in range(1,len(line)):
        t = (line[j].split(":"))
        for k in range(len(t)):
            scores.append(t[k])
    
    sum = 0
    meter = 0
    
    for j in range(1,len(scores),2):
        sum = sum + float(scores[j+1])
        u = [scores[j],float(scores[j+1])]
        tests.append(u)
        meter = meter + 1

    mean = sum/meter
    u = [scores[0],mean]
    students.append(u)

    
students.sort(key = lambda x:x[0])
tests.sort(key = lambda x:x[0])

result = [tests[0]]
result[0].append(1)
meter = 0



for i in range(1,len(tests)):
    if tests[i][0] == tests[i-1][0]:
        result[meter][1] = result[meter][1] + float(tests[i][1])
        result[meter][2] = result[meter][2] + 1
    else:
        result.append(tests[i])
        meter = meter + 1
        result[meter].append(1)
        
        
        
for i in range(len(students)):
    print(students[i][0],students[i][1])
    
    
for i in range(len(result)):
    print(result[i][0],result[i][1]/result[i][2])