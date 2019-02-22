import sys
from distance import score as distance_matrix, update
from q import score as q_matrix, new_node_distance
from sequence_file import read

# answers
neighbours = []

# Read list of sequences S
S = read("sequences.txt")

# Calculate distance matrix
D, labels = distance_matrix(S)

# program loop
while True:
    # Calculate Q matrix and minimum values
    Q, min = q_matrix(D)

    # Calculate distance of min values to new node
    f = min[0]
    g = min[1]
    f_label = labels[f]
    g_label = labels[g]
    dist_fu, dist_gu = new_node_distance(f, g, D)

    # update distance matrix D with new node
    D, labels = update(D, f, g, labels)

    # append results and correct for zero-indexed labelling, assignment requies 1-indexing
    neighbours.append([f_label + 1, labels[-1] + 1, dist_fu])
    neighbours.append([g_label + 1, labels[-1] + 1, dist_gu])

    # end condition, just 2 nodes left
    # just take distances between them
    if (len(D) == 2):
      neighbours.append([labels[0] + 1, labels[1] + 1, D[0][1]])
      neighbours.append([labels[1] + 1, labels[0] + 1, D[1][0]])
      break

for neighbour in neighbours:
  print(str(neighbour))

print("end")
"""
End Result
((0,3)5,2)7,(1,4),6) 
"""
