import urllib.request
import json
import time
from collections import Counter

import pdb

class AnalystScraper:

  def __init__(self, config, delay=4):
    self.recommendations_list = []
    self.analysts_info = None
    self.config = config
    self.delay = delay # don't accidentally DDOS them/hit rate limits.
                       # Normally needs to be between 3 and 15, depending
                       # on what's going on on their end

  def count_recommendations(self):
    self.__get_filtered_recommendations()
    return self.__final_countdown_dododooodooo()

  def print_analyst_info(self):
    print([(analyst['name'], analyst['rank']['ranked']) for analyst in self.analysts_info])

  def __get_filtered_recommendations(self):
    for analyst in self.config.filter_analysts(self.__get_analysts_info()):
      print('getting picks for {name}, rank {rank}'.format(name=analyst['name'], rank=analyst['rank']['ranked']))
      time.sleep(self.delay)
      try:
        self.__get_recommendations(analyst)
      except urllib.error.HTTPError:
        print('WE GOT CUT OFF, JIM')
        return self.__final_countdown_dododooodooo()

  def __get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info
    # pdb.set_trace()
    with urllib.request.urlopen(self.config.analysts_url()) as analysts:
      self.analysts_info = json.loads(analysts.read())
      self.print_analyst_info()
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


