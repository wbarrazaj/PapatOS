#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

import time
import sys

"""
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("r%d%%" % i)
    sys.stdout.flush()
"""

from tqdm import tqdm
for i in tqdm(range(100),ascii=True):
    time.sleep(0)