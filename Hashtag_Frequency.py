import commands
import collections
import json
import re

feed = open('test.txt', 'r').read()

def get_next_tweet(index):
	start_keyword = '#'
	end_keyword = "\"" or " "
	beginning_index = feed.find(start_keyword, index)
	end_index = feed.find(end_keyword, beginning_index)
	index = end_index
	return [index, feed[beginning_index+len(start_keyword):end_index]]


hashtag_list = []
hashtag_list_raw = re.findall("(^|[^0-9A-Z&/]+)(#|\uFF03)([0-9A-Z_]*[A-Z_]+[a-z0-9_\\u00c0-\\u00d6\\u00d8-\\u00f6\\u00f8-\\u00ff]*)",feed)
#note: for more info on this regex visit http://stackoverflow.com/questions/1563844/best-hashtag-regex

for hashtag in hashtag_list_raw:
	hashtag_list.append(hashtag[2])

for hashtag in collections.Counter(hashtag_list).most_common()[0:50]:
 	print hashtag