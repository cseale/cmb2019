
MATCH_SCORE = 2
MISMATCH_SCORE = -1
INDEL_SCORE = -1

def score(s_seq, t_seq):
  s_seq = "-" + s_seq
  m = len(s_seq)
  t_seq = "-" + t_seq
  n = len(t_seq)

  # empty score matrix
  s = [[], []]

  # initialise first row of needleman-wunch matrix
  s[0] = [i * INDEL_SCORE for i in range(0, m)]

  # initialise each row after
  for j in range(1,n):
    s[1] = [0] * m
    s[1][0] = j * INDEL_SCORE

    for i in range(1, m):
      # do alignment check
      if (s_seq[i] == t_seq[j]):
        s[1][i] = s[0][i-1] + MATCH_SCORE
      else:
        s[1][i] = s[0][i-1] + MISMATCH_SCORE
    
      sc = s[1 -1][i] + INDEL_SCORE
      if (sc > s[1][i]):
        s[1][i] = sc

      sc = s[1][i-1] + INDEL_SCORE
      if (sc > s[1][i]):
        s[1][i] = sc
    
    # replace s[0], only need to keep the last two rows
    s[0] = s[1]
  return s[1][i]