import random

marks = []

for i in range(1, 12):
    for j in range(4):
        scores = [random.randint(2, 5) for k in range(15)]
        marks.append(
            {
                'school_class': str(i) + ['а', 'б', 'в', 'г'][j],
                'scores': scores
            }
        )

all_scores = 0
all_scores_amt = 0

for m in marks:
    s = sum(m['scores'])
    a = len(m['scores'])
    all_scores += s
    all_scores_amt += a
    print('средний балл {}: {:1.1f}'.format(m['school_class'], s / a))
print('средний балл по школе: {:1.1f}'.format(all_scores / all_scores_amt))