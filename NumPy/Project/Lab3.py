
import numpy as np

data = np.genfromtxt('DATASet.csv', delimiter=",", skip_header=1)
# Let's assume 'age' is the 2nd column (index 1). Adjust index as needed:
ages = data[:, 1]

# Maximum age
max_age = np.nanmax(ages)
print("Find the max age and store it in a variable called 'max_age'.",max_age)

# Minimum age
min_age = np.nanmin(ages)
print("Find the min age and store it in a variable called 'min_age'.",min_age)


# Mean age
age_mean = np.nanmean(ages)
print("Find the mean of the age and store it in a variable called 'age_mean'.",age_mean)


# Standard deviation of age
age_std = np.nanstd(ages)
print("Find the standard deviation of the age and store it in a variable called 'age_std'",age_std)

# Create a subset of senior citizens
senior_citizens = data[data[:, 0] > 60]

# Optionally check how many senior citizens you have
len_seniors = len(senior_citizens)
print("Number of senior citizens:", len_seniors)


# Filter senior citizens: age > 60 (column index 0)
#senior_citizens = census[census[:, 0] > 60]

# Sum of working hours for senior citizens (column index 6)
working_hours_sum = np.sum(senior_citizens[:, 6])

# Number of senior citizens
senior_citizens_len = len(senior_citizens)

# Average working hours per week per senior
avg_working_hours = working_hours_sum / senior_citizens_len

print("Average working hours for senior citizens:", avg_working_hours)
if(avg_working_hours>25):
    print("it means the data indicates seniors are working more than the government-recommended limit of 25 hours per week")
else:
    print("it means the data indicates seniors are working as per the government-recommended limit of 25 hours per week")




