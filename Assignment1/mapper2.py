#!/usr/bin/env python
"""mapper.py"""

import sys
import string
import os

docid = os.path.splitext(os.path.basename(os.getenv('map_input_file')))[0]

# input comes from STDIN (standard input)
for line in sys.stdin:
	for word in line.strip().split():
        	lowered = word.lower()
        	filtered = filter(lambda c: 97 <= ord(c) <= 122, lowered)
		if len(filtered) > 0:
        		print '%s\t%s' % (docid, 1)
