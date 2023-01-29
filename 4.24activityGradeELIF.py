#Print the grade, given the marks

#input: marks, an interger from 0 to 100
marks = 40

#output: the grade, a string
if marks < 40:
    grade = 'fail'
elif marks >= 40 and marks <= 60:
    grade = 'pass'
elif marks > 60 and marks < 80:
    grade = 'merit'
else: # marks >= 80:
    grade = 'distinction'
print('The grade is', grade)
