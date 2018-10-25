# xfinity/comcast wordlist generator

AFAIK the xfinity keyspace is: 5 char word + 4 char number + 6 char word
ex: fever4759harbor

xfinity-keyspace.py - quick and shitty code to generate a wordlist for the xfinity wifi keyspace

wordlists - contains common 6 letter and 5 letter words as well as all 4 character numbers

sources and tools - contains original wordlists, source file on where to find words, as well as scripts to manipulate them.
	For the 5list.txt and 6list.txt wordlists, I downloaded the top 4000 english words and pulled out all the 5 and 6 character words into lists.

# sizes
keyspace.txt will come out to 75.2 GB in size. 12.2 GB as compressed tar.gz file.
