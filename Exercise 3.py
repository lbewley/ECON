import numpy as np

n = 100000

count = 0
for i in range(n):
    u, v = np.random.uniform(), np.random.uniform()
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)
    if d < 0.5:
        count +=1

area_estimate = count / n

print(area_estimate * 4) # Dividing by radius**2
