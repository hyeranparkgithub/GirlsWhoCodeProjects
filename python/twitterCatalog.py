import json

f = open("twitterData.json", "r")
tweetData = json.load(f)
f.close()

# print the id and text from the first tweet
for i in tweetData:
    print("ID is", i["id"])
    print("The tweet is:", i["text"])
