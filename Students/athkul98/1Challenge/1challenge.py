import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


def integersequence(num_outcomes=2,vec_length=1):
    # Return random integers from 0 to high (exclusive)
    #
    outcome = []
    for index in range(vec_length):
        outcome.append(np.random.random_integers(0,num_outcomes)) # EDIT
    return outcome


def distribution_sim(num_outcomes_ds=2,vec_length_ds=10):
    # Returns emmpirical distribution
    trial_num_ds = 10000
    empirical_dist_ds = np.zeros(vec_length_ds+1)

    for trial in range(0, trial_num_ds):
        outcome_ds = integersequence(num_outcomes_ds,vec_length_ds) # EDIT
        count_ones_ds = outcome_ds.count(1)
        empirical_dist_ds[count_ones_ds] += 1

    empirical_dist_ds = empirical_dist_ds/trial_num_ds
    return empirical_dist_ds
	
def distribution_sim1(num_outcomes_ds=2,vec_length_ds=10):
    # Returns emmpirical distribution
    trial_num_ds = 10000
    count_ones_ds1 = 0
    for trial in range(0, trial_num_ds):
        outcome_ds = integersequence(num_outcomes_ds,vec_length_ds) # EDIT
        count_ones_ds1 += outcome_ds.index(1)

    count_ones_ds1 = count_ones_ds1/10000
    return count_ones_ds1

# Create an empty horizontal vector
vec_length = 10
distributions = np.empty((0, vec_length+1))
print(distributions.shape)

for num_outcomes in range(2,21):
    empirical_dist = distribution_sim(2,10)
    # Add rows to horizontal vector
    distributions = np.append(distributions, [empirical_dist], axis=0)
    print(distributions.shape)

# Write output file
pd.DataFrame(distributions).to_csv("1challenge.csv")

print(distribution_sim1(2,1000))