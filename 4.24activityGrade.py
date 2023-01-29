#Print the grade, given the marks

#input: marks, an interger from 0 to 100
marks = 40

#output: the grade, a string
if marks < 40:
    grade = 'fail'
if marks >= 40 and marks <= 60:
    grade = 'pass'
if marks > 60 and marks < 80:
    grade = 'merit'
if marks >= 80:
    grade = 'distinction'
print('The grade is', grade)
