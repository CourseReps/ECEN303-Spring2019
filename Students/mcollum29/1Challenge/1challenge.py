import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

vec_length = 10

#Part 1:

def integersequence(num_outcomes=2,vec_length=1):
    # Return random integers from 0 to high (exclusive)
    #
    outcome = []
    for index in range(vec_length):
    	n = np.random.randint(low=0,high=num_outcomes)
    	outcome.append(n)
    return outcome

#Part 2:

def distribution_sim(num_outcomes_ds=2,vec_length_ds=10):
    # Returns emmpirical distribution
    trial_num_ds = 10000
    empirical_dist_ds = np.zeros(vec_length_ds+1)

    for trial in range(0, trial_num_ds):
        outcome_ds = integersequence(num_outcomes_ds,vec_length_ds)
        count_ones_ds = outcome_ds.count(1)
        empirical_dist_ds[count_ones_ds] += 1

    empirical_dist_ds = empirical_dist_ds/trial_num_ds
    return empirical_dist_ds

# Create an empty horizontal vector

distributions = np.empty((0, vec_length+1))
print(distributions.shape)

for num_outcomes in range(2,21):
    empirical_dist = distribution_sim(2,10)
    # Add rows to horizontal vector
    distributions = np.append(distributions, [empirical_dist], axis=0)
    print(distributions.shape)

# Write output file
pd.DataFrame(distributions).to_csv("1challenge.csv")

#Part 3:

#Extracts ones column from the distributions
one_dist = np.array([row[1] for row in distributions])
one_val = 0
one_avg = 0
i = 0

#Finds average distribution of ones
for x in np.ndenumerate(one_dist):
	one_val += x[1]
	i += 1

one_avg = one_val / i
print(one_avg)


	