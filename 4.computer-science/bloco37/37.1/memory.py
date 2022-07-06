#!/usr/bin/env python

import time

from resources import mem_total, mem_used


while(True):
    print(f"MemTotal: {mem_total} MB | MemUsed: {mem_used} MB")
    time.sleep(1)
