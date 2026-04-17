#!/usr/bin/env python
import random
import sys

print(" ".join([str(random.randint(0,int(sys.argv[1]))) for x in range(int(sys.argv[2]))]))
