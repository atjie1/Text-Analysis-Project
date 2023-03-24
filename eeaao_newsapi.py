from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='27cf3209c3f54fe7bc9e0dc8dabf271a')

all_articles = newsapi.get_everything(q='Everything Everywhere All at Once',
                                      from_param='2023-03-11',
                                      language='en',
                                      sort_by='relevancy')

print(all_articles['content'])

# ended up not using this API data