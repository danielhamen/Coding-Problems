import math
import os
import random
import re
import sys

def main(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


if __name__ == "__main__":
    n = int(input().strip())
    main(n)