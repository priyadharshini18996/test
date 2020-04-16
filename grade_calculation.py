
def solve(mark):
    
    for grade in mark:
        newMark = 0
        c = grade % 5
        if(grade >= 38 and 5-c < 3 and c != 0):
            newMark = grade + 5- c
            if (newMark > 100):
                newMark = 100
            print("student mark is:" ,str(newMark))
        else:
            newMark = grade
            print("student mark is:",str(newMark))


n = int(input().strip())
mark = []
mark_i = 0
for mark_i in range(n):
   mark_t = int(input().strip())
   mark.append(mark_t)
result = solve(mark)