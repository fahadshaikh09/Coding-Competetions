def afterDelete(sequence):
    i = 0
    while i < len(sequence)-1:
        if sequence[i] >= sequence[i+1]:
            return (sequence[i-1:i] + sequence[i+1:], sequence[i:i+1] + sequence[i+2:])
        i += 1

def isIncreasing(sequence):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return False
    return True

def almostIncreasingSequence(sequence):
    result = afterDelete(sequence)
    if result:
        seq1, se2 = result
        return isIncreasing(seq1) | isIncreasing(se2)
    else:
        return True

test_cases = [
    [1, 2, 1, 2],
    [1, 3, 2, 1],
    [1, 3, 2],
    [1, 1, 1, 2, 3],
    [0, -2, 5, 6],
    [1, 1],
]

for test in test_cases:
    print test, almostIncreasingSequence(test)