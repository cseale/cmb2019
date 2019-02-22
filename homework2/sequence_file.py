"""
Read sequence file
"""
def read(filename):
  sequences = []

  # file 
  f = open(filename, "r")

  for x in f:
    sequences.append(x.strip())

  return sequences