import math

# Define your array of five elements
array = [1, 1, 2, 2, 1]

# Calculate the GCD of all elements in the array using math.gcd
result = math.gcd(array[0], array[1])
# for i in range(2, len(array)):
#     result = math.gcd(result, array[i])

# 'result' now contains the GCD of all elements in the array
print("The GCD of the array is:", result)
