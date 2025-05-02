student_scores = [8 ,65 ,89, 86 ,55 ,91 ,64, 89,100]
max=student_scores[0]
i=1
for i in range(len(student_scores)):
    if max < student_scores[i]:
        max=student_scores[i]
print(max)