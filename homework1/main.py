import time

MATCH_SCORE = 1
MISMATCH_SCORE = -1
INDEL_SCORE = -1

def readSequenceFile(filename):
  # file 
  f = open(filename, "r")

  count = int(f.readline())
  sequence = ""

  for x in f:
    sequence += x.strip()

  return count, sequence

def scoreGlobalAlignment(s_seq, m, t_seq, n):
  s_seq = "-" + s_seq
  m = m + 1
  t_seq = "-" + t_seq
  n = n + 1

  # empty score matrix
  s = []

  # initialise first row of needleman-wunch matrix
  s.append([i * INDEL_SCORE for i in range(0, m)])

  # initialise each row after
  for j in range(1,n):
    s.append([0] * (m))
    s[j][0] = j * INDEL_SCORE

    for i in range(1, m):
      # do alignment check
      if (s_seq[i] == t_seq[j]):
        s[j][i] = s[j-1][i-1] + MATCH_SCORE
      else:
        s[j][i] = s[j-1][i-1] + MISMATCH_SCORE
    
      sc = s[j -1][i] + INDEL_SCORE
      if (sc > s[j][i]):
        s[j][i] = sc

      sc = s[j][i-1] + INDEL_SCORE
      if (sc > s[j][i]):
        s[j][i] = sc

  return s[j][i]

s_count, s_seq = readSequenceFile("testSeqT.txt")
t_count, t_seq = readSequenceFile("testSeqS.txt")

# record start time
start = time.time()
# generate score
global_score = scoreGlobalAlignment(s_seq, s_count, t_seq, t_count)
# record end time
end = time.time()
running_time = end - start
# done
print("Running Time: " + str(running_time))
print("Final Score: " + str(global_score))