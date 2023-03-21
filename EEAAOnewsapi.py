import requests
import config

url = ('https://newsapi.org/v2/everything?'
       'q=Everything Everywhere All at Once&'
       'from=2023-03-11&'
       'sortBy=popularity&'
       'apiKey=27cf3209c3f54fe7bc9e0dc8dabf271a')

response = requests.get(url)
print(response.json())