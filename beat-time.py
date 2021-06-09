#!/usr/bin/env python3
# Swatch "BEAT" time, anchored on UTC rather than UTC+01
import time

now = int(time.time()) % 86400) / 86.4

## Format the time as @beat with two decimal points:
# print("@{:.2f}".format(now))

## Round down to whole @beat
print(int(now))
