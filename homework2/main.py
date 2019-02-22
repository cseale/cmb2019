import sys
from distance import score as distance_matrix, update
from q import score as q_matrix, new_node_distance

def readSequenceFile(filename):
  sequences = []

  # file 
  f = open(filename, "r")

  for x in f:
    sequences.append(x.strip())

  return sequences

# Read list of sequences S
S = readSequenceFile("sequences.txt")

# Calculate distance matrix
D = distance_matrix(S)

print("Length of original matrix: " + str(len(D)))

# Calculate Q matrix and minimum values
Q, min = q_matrix(D)

# Calculate distance of min values to new node
f = min[0]
g = min[1]
dist_fu, dist_gu = new_node_distance(f, g, D)

# update distance matrix D with new node
D = update(D, f, g)

print("Length of current matrix: " + str(len(D)))


print("end")
