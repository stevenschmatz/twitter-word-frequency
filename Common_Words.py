import commands
import collections
import json

get_feed = "twurl -t -H stream.twitter.com /1.1/statuses/sample.json -t 1 > test.txt"
feed = open('test.txt', 'r').read()

def get_next_tweet(index):
	start_keyword = '\"text\"'
	end_keyword = "\","
	beginning_index = feed.find(start_keyword, index)
	end_index = feed.find(end_keyword, beginning_index)
	index = end_index
	return [index, feed[beginning_index+len(start_keyword)+2:end_index]]

def get_n_tweets(n):
	i = 0
	index = 0
	tweets = []
	while i < n:
		tweet = get_next_tweet(index)
		tweets.append(tweet[1])
		index = tweet[0]
		i += 1
	return tweets

tweet_list = get_n_tweets(4000)
word_list = []
for tweet in tweet_list:
	for word in tweet.split(" "):
		word_list.append(word)

for word in collections.Counter(word_list).most_common()[0:100]:
 	print word