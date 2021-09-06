import urllib.request
import json
import time
from collections import Counter
import pdb

class ThingDoer:

  def __init__(self, analysts_url='', stocks_url='', stocks_url_identifier='', filter_function=None):
    self.recommendations_list = []
    self.analysts_info = None
    self.analysts_url = analysts_url
    self.stocks_url = stocks_url
    self.stocks_url_identifier = stocks_url_identifier
    self.filter_function = filter_function

  def count_recommendations(self):
    self.__get_filtered_recommendations()
    return Counter(self.recommendations_list)

  def __get_filtered_recommendations(self):
    for analyst in self.__get_analysts_info():
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(3) # don't accidentally DDOS them/hit rate limits
      if self.filter_function:
        return self.filter_function(self.__get_recommendations(analyst))
      else:
        return self.__get_recommendations(analyst)

  def __get_analysts_info(self):
    if self.analysts_info is not None:
      return self.analysts_info

    with urllib.request.urlopen(self.analysts_url) as analysts:
      self.analysts_info = json.loads(analysts.read())
      return self.analysts_info

  def __get_recommendations(self, analyst):
    stock_evaluations = self.__get_analyst_evaluations(analyst)
    self.recommendations_list += [stock['name'] for stock in stock_evaluations if self.__is_recommended(stock)]

  def __is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

  def __get_analyst_evaluations(self, analyst):
    identifier = analyst[self.stocks_url_identifier].lower().replace(' ', '-')
    with urllib.request.urlopen(self.stocks_url + self.stocks_url_identifier + '=' + identifier) as analyst_stocks:
      return json.loads(analyst_stocks.read())
