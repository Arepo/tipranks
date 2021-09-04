import urllib.request
import json

class TipRanksScraper:

  def __init__(self):
    print('hello world')

  def get_analysts_page(self):
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general'
      ) as response:
      self.analysts_page = json.loads(response.read())
    print(self.analysts_page)

  def extract_analyst_urls(self):
    get_analysts_page()


scraper = TipRanksScraper()
scraper.get_analysts_page()

