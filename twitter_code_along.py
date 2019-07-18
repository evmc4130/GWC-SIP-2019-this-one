'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()


#----------------
import matplotlib.pyplot as plt
plt.bar([1,3,5,7,9], [5,2,7,8,2], label = "example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label = "example two", color = 'g')
#
# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
print("Tweet id: ", tweetData[0]["id"])

# First ask students how they might print the text object:
# Then show them the following code
print("Tweet text: ", tweetData[0]["text"])


# First ask students how might they use loops
# to print the ["text"] of all the tweets:

# Show them the following two options:

# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
# #
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.

sum = 0
num = 0
for tweet in tweetData:
	if "favorite_count" not in tweet:
		print("missing")
	else:
		print(tweet["favorite_count"])
		num += 1
		sum += tweet["favorite_count"]
avg = sum/num
print(avg)


textList = []

for i in range(len(tweetData)):
	temptweet = tweetData[i]["text"]
	textList.append(temptweet)
print(textList)


# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.



tb = TextBlob("you are a brilliant computer scientist.")

print(tb.polarity)


polarityList = []
for i in textList:
	blob1 = TextBlob(i)
	polar1 = blob1.polarity
	polarityList.append(polar1)
print(polarityList)

leest = []
for i in range(len(tweetData)):
	dictionaree = {}
	dictionaree["t_id"] = tweetData[i]['id']
	dictionaree["polarity"] = polarityList[i]
	dictionaree["tweet"] = textList[i]
	leest.append(dictionaree)


tweetstring = ""
for tweet in textList:
	tweet = tweet + ""
	tweetstring += tweet
print(tweetstring)
tString = ""
for tweet in textList:
	tString += tweet + ' '
wordcloud = WordCloud().generate(tweetstring)
plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud, interpolation = "biliniear")
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
