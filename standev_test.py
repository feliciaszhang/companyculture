import numpy as np
import pandas as pd
import statistics
dataset= [200,-90,10,12,10,10,100,12,13,15,10]

print(dataset)
dataset= sorted(dataset)
q1, q3= np.percentile(dataset,[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr)

for y in dataset:
    if(y>upper_bound or y<lower_bound):
        print(y)
        dataset.remove(y)
print(dataset)

    
#is overall score positive or negative?
overallscore = 0.0
for i in range(len(dataset)):
    overallscore += dataset[i]

print(overallscore)
