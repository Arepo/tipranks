import urllib.request
import json
import time
from collections import Counter, namedtuple
import collections
import pdb

class RetailScraper:

  def __init__(self):
    self.analysts_info = None
    self.recommendations_list = []

  def get_good_analysts_info(self, min_success_rate=0.8):
    return [analyst for analyst in self.get_analysts_info() if analyst['recommendations']['ratio'] > min_success_rate]

  def get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info

    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts=100'
    ) as analysts:
      self.analysts_info = json.loads(analysts.read())
      return self.analysts_info

  def get_analyst_evaluations(self, analyst):
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id={}'.
      format(analyst['expertPortfolioId'])
    ) as analyst_stocks:
      return json.loads(analyst_stocks.read())['allocation']['byCompany']

  def get_recommendations(self, analyst):
    stock_holdings = self.get_analyst_evaluations(analyst)
    self.recommendations_list += [stock['companyName'] for stock in stock_holdings if stock['percent'] > 0.01]

  def get_good_recommendations(self):
    self.recommendations_list = []
    for analyst in self.get_good_analysts_info():
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(3) # don't accidentally DDOS them/hit rate limits
      self.get_recommendations(analyst)

  def count_recommendations(self):
    self.get_good_recommendations()
    print(Counter(self.recommendations_list))


ScraperConfig = collections.namedtuple('ScraperConfig', ['analysts_url'])

# wall_st_config = ScraperConfig(
#   analysts_url = 'https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general&numExperts=100'
#   stocks_url =
# )

# retail_config = ScraperConfig(
#   analysts_url = 'https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts=100',
#   stocks_url = 'https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id=710095&break=1630924585109'
# )


scraper = RetailScraper()
scraper.count_recommendations()
