#!/usr/bin/env python
"""mapper.py"""

import sys
import string
import os

docid = os.path.splitext(os.path.basename(os.getenv('map_input_file')))[0]

# input comes from STDIN (standard input)
for line in sys.stdin:
	key, count = line.split('\t',1)
	docid, term = key.split('+',1)
	print '%s\t%s\t%s' % (docid, term, count)

