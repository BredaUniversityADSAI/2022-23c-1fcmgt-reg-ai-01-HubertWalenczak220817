import DuckDuckGoImages as ddg
def scrape(query):
    ddg.download(query, folder='./prepareData/'+query, max_urls=1000)

scrape('crop field -animal -animals -human -humans')
scrape('plains -animal -animals -human -humans')
scrape('forest -animal -animals -human -humans')
scrape('city -animal -animals -human -humans')

