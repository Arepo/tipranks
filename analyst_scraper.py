import urllib.request
import json
import time
import random
from datetime import date
from collections import Counter

import pdb

class AnalystScraper:

  def __init__(self, config, delay=None):
    self.recommendations_list = []
    self.analysts_info = None
    self.config = config
    self.delay = delay # don't accidentally DDOS them/hit rate limits.
                       # Normally needs to be between 3 and 15, depending
                       # on what's going on on their end

  def count_recommendations(self):
    self.__get_filtered_recommendations()
    return self.final_countdown_dododooodooo()

  def print_analyst_info(self):
    print([(analyst['name'], analyst['rank']['ranked']) for analyst in self.analysts_info])

  def __get_filtered_recommendations(self):
    for analyst in self.config.filter_analysts(self.get_analysts_info()):
      print('getting picks for {name}, rank {rank}'.format(name=analyst['name'], rank=analyst['rank']['ranked']))
      if self.delay:
        time.sleep(self.delay)
      else:
        delay = random.randrange(16, 47)
        time.sleep(delay)
      try:
        self.__store_recommendations(analyst)
      except urllib.error.HTTPError:
        print('WE GOT CUT OFF, JIM')
        return self.final_countdown_dododooodooo()

  def get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info
    with urllib.request.urlopen(self.config.analysts_url()) as analysts:
      self.analysts_info = json.loads(analysts.read())
      # self.print_analyst_info()
      return self.analysts_info

  def __store_recommendations(self, analyst):
    stock_evaluations = self.config.evaluations_from_analyst(
      self.__get_analyst_evaluations(analyst)
    )
    self.config.write_to_csv(analyst, stock_evaluations, date)
    self.recommendations_list += [self.config.get_stock_identity(stock) for stock in stock_evaluations if self.config.is_recommended(stock)]

  def __get_analyst_evaluations(self, analyst):
    with urllib.request.urlopen(self.config.stocks_url(analyst)) as analyst_stocks:
      return json.loads(analyst_stocks.read())

  def final_countdown_dododooodooo(self):
    return Counter(self.recommendations_list)


