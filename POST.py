import requests # Imports python HTTP requests library

headers = {"Authorization": "Basic Base64_Encoded_Consumer_String", # See GitHub page for details of how to generate this
           "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"} # Defines the payload that the requests contains

data = {"grant_type": "client_credentials"} # Informs API what is desired from the request
r = requests.post("https://api.twitter.com/oauth2/token", headers = headers, data = data) # Makes a post request to api.twitter.com
print(r.text) # Prints the data returned by the post request
