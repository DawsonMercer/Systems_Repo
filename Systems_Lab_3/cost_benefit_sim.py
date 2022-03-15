import random 
import time
'''
Please see the comments below. 
Caution: This is just a small example/prototype. You are required to
 write the code by following 
instructions/questions given in lab #3. 
Lets consider that there are two cost elements and three benefit elements.
It important to understand that number of cost and beenfit elements need not be the same. 
Cost and benefit values are specified in $. 
'''
t_start=time.time()
# Cost elements. These are the maximum amounts the company is required to 
# pay when the probability is equal to one. 
c1 = 75000 
c2 = 10000

# Benefit elements. These are the maximum amounts the company  could earn
#  when the probability is equal to one. 
b1 = 10000
b2 = 80000
b3 = 50000 

# Minimum and maximum probability values of costs. 

# For cost 1 .It means that the probability of cost element c1 could vary from 0.30 to 0.90 
cp1_min = 0.30 
cp1_max = 0.90 

# cost 2 
cp2_min = 0.20 
cp2_max = 0.95

# Minimum and maximum probability values of benefits. 

# For benefit #1 
bp1_min = 0.30 
bp1_max = 0.90

# For benefit # 2 
bp2_min = 0.20
bp2_max = 0.95

# For benefit # 3
bp3_min = 0.05
bp3_max = 0.24

# Maximum number of Simulations. 
sim_max= 100000

# Accumulate the cost and benefit over the simulations. 
cost_total_1 = 0
cost_total_2 = 0

benefit_total_1 = 0 
benefit_total_2 = 0 
benefit_total_3 = 0 

# counter = 1

for ind in range( 0, sim_max-1) :

    cost_total_1 =cost_total_1+ c1*random.uniform(cp1_min,cp1_max)
    cost_total_2 =cost_total_2+ c2*random.uniform(cp2_min,cp2_max)

    benefit_total_1=benefit_total_1+b1*random.uniform(bp1_min,bp1_max)
    benefit_total_2=benefit_total_2+b2*random.uniform(bp2_min,bp2_max)
    benefit_total_2=benefit_total_2+b3*random.uniform(bp3_min,bp3_max)
    # counter+=1


# Calculate average cost and benefit. 

# Average costs.
average_cost_1 = cost_total_1/sim_max
average_cost_2 = cost_total_2/sim_max
print("average cost 1", average_cost_1)
print("average cost 2", average_cost_2)


# Average benefits.
average_benefit_1 = benefit_total_1/sim_max
average_benefit_2 = benefit_total_2/sim_max
average_benefit_3 = benefit_total_3/sim_max

# Calculate the total cost and total benefit.
# Don't divide total_cost and total benefit by # of simulations.
total_cost = average_cost_1+average_cost_2
total_benefit = average_benefit_1+average_benefit_2+average_benefit_3

# print the total cost and total benefit
print("Total cost is $",total_cost)
print("Total  benefit is $",total_benefit)

if (total_cost <= total_benefit):
    print("Project could be approved!")
else:
    print("Project disapproved.")
        
print("Time needed for code execution in mSec",1000*(time.time()-t_start))
# print(f"Counter: {counter}")


