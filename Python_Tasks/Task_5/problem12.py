# Problem 12 : Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    result = []
    for word in words:
        if len(word) > 0:
            word = word[0].upper() + word[1:]
        result.append(word)
    return ' '.join(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
