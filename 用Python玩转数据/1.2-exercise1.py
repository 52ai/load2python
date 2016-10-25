# coding:utf-8

print "Score Grade:"
score_grade = input()

if 100 >= score_grade >= 90:
    print "A"
elif 89 >= score_grade >= 70:
    print "B"
elif 69 >= score_grade >= 60:
    print "C"
elif 59 >= score_grade >= 0:
    print "D"
else:
    print "Invalid score!"
