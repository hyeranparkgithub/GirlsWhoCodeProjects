'''
In this project, you will visualize the feelings and language used in a set of
Tweets.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud


tweetFile = open("twitterData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarityTotal = []
subjectivityTotal = []


oneLargeString = ""

filtWords = ["https", "about", "like", "make", "thing"]

for i in tweetData:
    # print("ID is", i["id"])
    # print("The tweet is:", i["text"])
    tb = TextBlob(i["text"])
    polarity = tb.polarity
    # print("The polarity is", polarity)
    subjectivity = tb.subjectivity
    # print("The subjectivity is", subjectivity)
    polarityTotal.append(polarity)
    subjectivityTotal.append(subjectivity)
    oneLargeString = oneLargeString + i["text"]

oneLargeString = TextBlob(oneLargeString)

for a in oneLargeString:
    if oneLargeString.words.count(filtWords, case_sensitive = False)
        if len(a) < 3:
            if a not in filtWords:
                if (a.isalpha()) == True:
                    wordcloud = WordCloud(max_font_size=40).generate(oneLargeString)

plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()












print("\n")
print("\n")

averagePolarity = sum(polarityTotal)/len(polarityTotal)
averageSubjectivity = sum(subjectivityTotal)/len(subjectivityTotal)
print("The average polarity is", averagePolarity)
print("The average subjectivity is", averageSubjectivity)



plt.hist(polarityTotal, facecolor = "gray", bins=[-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.title('Histogram of Polarities')
plt.axis([-0.6, 1, 0, len(polarityTotal)])
plt.grid(True)
plt.show()

plt.hist(subjectivityTotal, facecolor = "green", bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.xlabel('Subjectivity')
plt.ylabel('Frequency')
plt.title('Histogram of Subjectivity')
plt.axis([0, 1, 0, len(subjectivityTotal)])
plt.grid(True)
plt.show()
