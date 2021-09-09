import urllib.request
import json
import time
from collections import Counter
# Delete the periods to run as script
from .wall_st_config import WallStConfig
from .retail_config import RetailConfig
from .hedge_fund_config import HedgeFundConfig
import pdb

class AnalystScraper:

  def __init__(self, config):
    self.recommendations_list = []
    self.analysts_info = None
    self.config = config

  def count_recommendations(self):
    self.__get_filtered_recommendations()
    return self.__final_countdown_dododooodooo()

  def print_analyst_info(self):
    print([(analyst['rank']['ranked'], analyst['sectorId']) for analyst in self.analysts_info])

  def __get_filtered_recommendations(self):
    for analyst in self.config.filter_analysts(self.__get_analysts_info()):
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(3) # don't accidentally DDOS them/hit rate limits
      try:
        self.__get_recommendations(analyst)
      except urllib.error.HTTPError:
        print('WE GOT CUT OFF, JIM')
        return self.__final_countdown_dododooodooo()

  def __get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info

    with urllib.request.urlopen(self.config.analysts_url()) as analysts:
      self.analysts_info = json.loads(analysts.read())

      return self.analysts_info

  def __get_recommendations(self, analyst):
    stock_evaluations = self.config.evaluations_from_analyst(
      self.__get_analyst_evaluations(analyst)
    )
    self.recommendations_list += [self.config.get_stock_identity(stock) for stock in stock_evaluations if self.config.is_recommended(stock)]

  def __get_analyst_evaluations(self, analyst):
    with urllib.request.urlopen(self.config.stocks_url(analyst)) as analyst_stocks:
      return json.loads(analyst_stocks.read())

  def __final_countdown_dododooodooo(self):
    return Counter(self.recommendations_list)

# scraper = AnalystScraper(RetailConfig(number_of_analysts=50, min_success_rate=0.8, min_stock_percent=0.02))
# scraper = AnalystScraper(WallStConfig(number_of_analysts=100, stock_identifier='ticker', sector='general'))
# scraper = AnalystScraper(HedgeFundConfig(number_of_analysts=25, stock_identifier='name', min_stock_percent=0))
# print(scraper.count_recommendations())
