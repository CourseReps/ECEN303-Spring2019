import numpy as np
import pandas as pd

def integersequence(num_outcomes=2, vec_length=1):
	
	outcome=[]
	for index in range(vec_length):
		outcome.append(np.random.randint(0,num_outcomes)) # Edited
	return outcome

# print(integersequence(5,10)) # used for testing

def distribution_sim(num_outcomesd=2, vec_lengthd=10):

	trial_numd = 10000
	empirical_distd = np.zeros(vec_lengthd+1)

	for trial in range (0, trial_numd):
		outcome = integersequence(num_outcomesd,vec_lengthd) # Edited
		count_onesd = outcome.count(1)
		empirical_distd[count_onesd] += 1

	empirical_distd = empirical_distd/trial_numd
	return empirical_distd

vec_lengthd = 10
distributions = np.empty((0, vec_lengthd+1))
print(distributions.shape)

for num_outcomes in range (2,21):
	empirical_dist = distribution_sim(2,10)
	distributions = np.append(distributions, [empirical_dist], axis=0)
	print(distributions.shape)

pd.DataFrame(distributions).to_csv("1challenge.csv")

num_outcomes=2
vec_length=10

tmp=integersequence(num_outcomes,vec_length)
avg=tmp.count(1)/float(vec_length) 
rg=num_outcomes-1 # because it's exclusive

print "In one simulation, there was a" ,avg, "chance of getting a one between 0 and" ,rg, "in" ,vec_length, "many tries."

per_ones=1.0-empirical_dist[1] # 1.0 - chance of getting 0 ones
print "In 10,000 simulations, chance of finding a one in any of those simulations was", per_ones

