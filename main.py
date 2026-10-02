import numpy as np 

marks = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

# total marks and avg

total = np.sum(marks,axis=1)
avg = np.mean(marks,axis=1)

criteria = np.any(marks > 8, axis=1)
pa_criteria = np.where(criteria)[0]+1

print(f"student{pa_criteria} has 8 in atleast one subject")