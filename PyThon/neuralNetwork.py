import random
import math

weight = random.random()
#print(weight)
input = [[0.21, 0.34, 0.12, 0.54], [0.67, 0.67, 0.78, 0.34], [0.45, 0.54, 0.56, 0.12], [0.23, 0.45, 0.34, 0.77]]
#print(input[0])
n1 = ( (input[0][0] * weight) + (input[0][1] * weight) + (input[0][2] * weight) + (input[0][3] * weight)) + 0.34
n2 = ( (input[1][0] * weight) + (input[1][1] * weight) + (input[1][2] * weight) + (input[1][3] * weight)) + 0.23
n3 = ( (input[2][0] * weight) + (input[2][1] * weight) + (input[2][2] * weight) + (input[2][3] * weight)) + 0.73
n4 = ( (input[3][0] * weight) + (input[3][1] * weight) + (input[3][2] * weight) + (input[3][3] * weight)) + 0.29
#print(n1)
value1 = (1/(1 + math.exp(-n1)))
value2 = (1/(1 + math.exp(-n2)))
value3 = (1/(1 + math.exp(-n3)))
value4 = (1/(1 + math.exp(-n4)))

newValue = (value1 * weight) + (value2 * weight) + (value3 * weight) + (value4 * weight) + 0.67

output = (1/(1 + math.exp(-newValue)))
print("Output: ", output)