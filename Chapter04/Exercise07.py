"""
Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
"""
try:
    score = float(input('Enter score: '))
except:
    print('bad score')
    quit()

def computegrade(score):
    if 0 <= score <= 1:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'
    else:
        return 'Bad score'

grade = computegrade(score)
print(grade)