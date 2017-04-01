# Python-Twitter-API
Python code for accessing and retrieving data from the Twitter API
# POST Request
The POST request must be made first to gain the bearer token from Twitter's servers. To make the request you must create a Twitter app (https://apps.twitter.com/). After the app is made, copy the following information:
* Twitter API consumer key
* Twitter API consumer secret
These are unique to each app created. The consumer key and secret must then be concatenated together sperated by a colon, as shown below:

Consumer secret = xxx111

Consumer key = 111xxx

Consumer secret:Consumer key

xxx111:111xxx

This concatenated string must then be base 64 encoded (https://www.base64encode.org/).

The base 64 encoded string can then be inserted into the POST request code replacing the text "Base64_Encoded_Consumer_String" in line 3 of POST.py.

When run, the program will return the bearer token.

# GET Request
The GET request makes a request to the Twitter API for data and the API replies. The bearer token from the POST request must be instered in place fo the text "Bearer_Token_Goes_Here" in line 19 of GET.py.
The URL in the function "requests.get" can be changed to aquire different information, see https://dev.twitter.com/rest/public/search for details on what variables can be passed into the URL. 
