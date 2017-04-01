import json # For processing the data returned by the API in an effective way
import requests # For making the request to the API

def log(data):
    dataFile = open("data.txt", "a") # Opens data.txt and prepares to append it
    dataFile.write(data) # Writes data to the file
    dataFile.close() # Closes the file

def clean(data):
    data = data.encode("ascii", "replace") # Encodes the data to ascii and replaces any characters it can't encode with question marks
    data = data.decode("utf-8") # Decodes the data back into utf-8
    if "&amp" in data:
            data = data.replace("&amp;", "&") # Replaces &amp; with & (ampesands appear as &amp; in the Twitter API data)
    return data

count = "20" # Sets the number of tweets requested to 20
accountName = "@MartinRiis_" # Sets the account name
hashtag = "%23" + "hashtag" # Sets the hashtag (%23 is the URL encoded version of "#")
headers = {"Authorization": "Bearer Bearer_Token_Goes_Here"} # Passes the bearer token as a header in the request

r = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=from" + accountName + hashtag + "&count=" + count, headers = headers) # Sends the request to the API

rStr = json.loads(r.text) # Loads the tweet data in json format

try:
    for element in rStr["statuses"]:
        user = "User: " + element["user"]["screen_name"] # Sets variable user to the data stored within "screen_name"
        user = clean(user)
        print(user + "\n")
        log(user + "\n")

        text = element["text"] # Sets the variable text to the data stored within "text"
        text = clean(text)
        log(text + "\n")
        print("Tweet: " + text + "\n")

        dateTime = "Created at: " + element["created_at"] + "\n" # Sets the variable dateTime to the data stored within "created_at"
        log(dateTime + "\n")
        print(dateTime)

except KeyError: 
    print("Error! Data was not received, check your bearer token is valid")
