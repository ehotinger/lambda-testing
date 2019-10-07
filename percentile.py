import numpy as np

arr = []
filepath = 'numbers.txt'
with open(filepath) as fp:
   line = fp.readline().strip()
   while line:
    arr.append(float(line))
    line = fp.readline().strip()

# print arr
print("Overhead from Step Functions + Lambda in seconds")
print("p25: {}".format(np.percentile(arr, 25)))
print("p50: {}".format(np.percentile(arr, 50)))
print("p75: {}".format(np.percentile(arr, 75)))
print("p90: {}".format(np.percentile(arr, 90)))
print("p99: {}".format(np.percentile(arr, 99)))