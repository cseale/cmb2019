"""
Return Q matrix
"""
def score(D):
    n = len(D)
    Q = []
    min = [0, 0, float("inf")]

    # initialise empty matrix
    for i in range(n):
        Q.append([0] * n)

    for i in range(n):
        for j in range(i+1, n):
            myscore = q(i, j, n, D)
            Q[i][j] = myscore
            Q[j][i] = myscore

            if (myscore < min[2]):
                min = [i, j, myscore]

    return Q, min


"""
Return Q value
"""
def q(i, j, n, D):
    first_term = (n-2)*D[i][j]
    second_term = 0
    third_term = 0
    for k in range(n):
        second_term += D[i][k]
        third_term += D[j][k]

    return first_term - second_term - third_term

def new_node_distance(f, g, D):
    n = len(D)
    first_term = 0.5*D[f][g]
    second_term = 0
    third_term = 0
    for k in range(n):
        second_term += D[f][k]
        third_term += D[g][k]

    dist_fu = first_term + (second_term - third_term)/(2*(n - 2))
    dist_gu = D[f][g] - dist_fu

    return dist_fu, dist_gu

