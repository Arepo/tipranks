import urllib.request
import json
import time
from collections import Counter
from .thing_doer import ThingDoer


class RetailScraper:

  def __init__(self, thing_doer=None, number_of_analysts=100):
    self.thing_doer = thing_doer or ThingDoer(number_of_analysts)

  def count_recommendations(self):
    self.thing_doer.count_recommendations()

  def __get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info

    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts={}'
        .format(self.number_of_analysts)
    ) as analysts:
      self.analysts_info = json.loads(analysts.read())
      return self.analysts_info

  def __get_good_analysts_info(self, min_success_rate=0.8):
    return [analyst for analyst in self.__get_analysts_info() if analyst['recommendations']['ratio'] > min_success_rate]

  def __get_analyst_evaluations(self, analyst):
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id={}'.
      format(analyst['expertPortfolioId'])
    ) as analyst_stocks:
      return json.loads(analyst_stocks.read())['allocation']['byCompany']

  def __get_recommendations(self, analyst):
    stock_holdings = self.__get_analyst_evaluations(analyst)
    self.recommendations_list += [stock['companyName'] for stock in stock_holdings if stock['percent'] > 0.01]

  def __get_filtered_recommendations(self):
    for analyst in self.__get_good_analysts_info():
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(3) # don't accidentally DDOS them/hit rate limits
      self.__get_recommendations(analyst)




# scraper = RetailScraper()
# scraper.count_recommendations()
