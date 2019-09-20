#!/bin/python3

import os
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1Ctr = Counter(s1)
    s2Ctr = Counter(s2)
    return 'NO' if len(s1Ctr) + len(s2Ctr) == len(s1Ctr + s2Ctr) else 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
