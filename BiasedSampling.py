import random
import pandas as pd

# create samples for a given discrete probability distribution
input_prob = [0.3, 0.45, .25]
sample = []
for i in range(1000000):
    num = random.random()
    for k in range(3):
        num -= input_prob[k]
        if num <= 0:
            sample.append(k)
            break
pd.Series(sample).value_counts()



