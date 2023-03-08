import DuckDuckGoImages as ddg
def scrape(query):
    ddg.download(query, folder='./prepareData/'+query, max_urls=1000)

scrape('white man')
scrape('white woman')
scrape('black man')
scrape('black woman')
scrape('asian man')
scrape('asian woman')

scrape('wild boar')
scrape('dear')
scrape('wolf')
scrape('fox')
