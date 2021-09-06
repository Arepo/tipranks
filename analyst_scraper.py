import urllib.request
import json
import time
from collections import Counter
import pdb

class AnalystScraper:

  def __init__(self, config):
    self.recommendations_list = []
    self.analysts_info = None
    self.config = config

  def count_recommendations(self):
    self.__get_filtered_recommendations()
    return Counter(self.recommendations_list)

  def __get_filtered_recommendations(self):
    for analyst in self.config.filter_analysts(self.__get_analysts_info()):
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(3) # don't accidentally DDOS them/hit rate limits
      return self.__get_recommendations(analyst)

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
    self.recommendations_list += [stock[self.config.stock_identifier] for stock in stock_evaluations if self.config.is_recommended(stock)]

  def __get_analyst_evaluations(self, analyst):
    with urllib.request.urlopen(self.config.stocks_url(analyst)) as analyst_stocks:
      return json.loads(analyst_stocks.read())
