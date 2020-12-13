#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
doc_id_list = []
old_docid = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, docid = line.split('\t', 1)

    # convert count (currently a string) to int
    #try:
        #count = int(count)
    #except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        #continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
	if docid not in doc_id_list:
		doc_id_list.append(docid)
        #current_count += count
    else:
        if current_word:
		if docid not in doc_id_list:
			doc_id_list.append(docid)	
            	# write result to STDOUT
            	print '%s\t%s' % (current_word, len(doc_id_list))
        doc_id_list = []
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, len(doc_id_list))
