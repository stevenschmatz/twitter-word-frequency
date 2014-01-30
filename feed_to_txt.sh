doalarm () { perl -e 'alarm shift; exec @ARGV' "$@"; }
doalarm 10 twurl -t -H stream.twitter.com /1.1/statuses/sample.json -t 1 > test.txt