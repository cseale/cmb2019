from alignment import score as alignment_score

"""
Return a distance matrix
"""
def score(S):
    D = []
    labels = list(range(len(S)))

    # initialise empty matrix
    for i in labels:
        D.append([0] * len(S))

    for i in labels:
        for j in range(i+1, len(S)):
            myscore = alignment_score(S[i], S[j])
            D[i][j] = myscore
            D[j][i] = myscore

    return D, labels

"""
Update distance matrix with new scores
"""
def update(D, f, g, labels):
    n = len(D)
    dist_u = []

    labels.append(labels[-1] + 1)

    # calculate new scores and append to end
    for k in range(n):
        dist_uk = 0.5*(D[f][k] + D[g][k] - D[f][g])
        dist_u.append(dist_uk)
        D[k].append(dist_uk)
    dist_u.append(0)
    D.append(dist_u)

    # delete elements of old matrix
    indices = [f, g]
    # first delete rows in reverse order
    for j in sorted(indices, reverse=True):
        del D[j]
        del labels[j]

    # then delete columns of each row in reverse order
    for i in range(len(D)):
        for j in sorted(indices, reverse=True):
            del D[i][j]

    return D, labels
