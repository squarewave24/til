A = "zabc"
B = "zdef "
C = "zdef zabc"

def helper(A, B, C, i, j, k):
    if k == len(C) and i == len(A) and j == len(B):
        return True
    
    option1, option2 = False, False
    if i < len(A) and A[i] == C[k]:
        option1 = helper(A, B, C, i + 1, j, k + 1)
    if j < len(B) and B[j] == C[k]:
        option2 = helper(A, B, C, i, j + 1, k + 1)
    return option1 or option2


def is_interleave(A, B, C):
    # assert False, 'testing'

    if len(A) + len(B) != len(C):
        return False
    return helper(A, B, C, 0, 0, 0)


print(is_interleave(A, B, C))