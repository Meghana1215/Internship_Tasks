# Problem 19 : Company Logo.
# https://www.hackerrank.com/challenges/most-commons/problem


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, frequency in result[:3]:
        print(char, frequency)
