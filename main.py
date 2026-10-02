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
highest = np.argmax(total)
lowest = np.argmin(total)

print(f"topper: student{highest+1} with total marks {total[highest]}")
print(f"lowest: student {lowest+1} with lowest marks {total[lowest]}")

