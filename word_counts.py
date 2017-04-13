import sys

#create a dictionary to store the count of each word
wordcount = {}

#store file from command line in variable file
file = sys.stdin

#loop over the contents of the file and split it into words
for line in file:
	line = line.strip()
	words = line.split()

	#loop over the contents of words and parse out individual words in it 
	#check if new variable word is not in the dictionary. 
	#if so, mark it as appearing once. Add 1 for each occurance of the word. 
	for word in words:
		if word not in wordcount: 
			wordcount[word] = 1
		else:
			wordcount[word] += 1

print wordcount

#sort dictrionary keys (words) by value, largest to smallest
wordtuple = [(word, count) for count, word in sorted
		([(count, word) for word, count in wordcount.items()], reverse=True
	)
]

#pair down the contents to make the results manageable. Developer changes 
#the boundaries
for word, count in wordtuple:
	if count < 150 and count > 30:
		print word #+ " : " + str(count)
