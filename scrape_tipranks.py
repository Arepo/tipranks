import urllib.request
import json
import time
from collections import Counter, namedtuple
import collections



class TipRanksScraper:

  def __init__(self):
    self.recommendations_list = []

  def get_analysts_info(self):
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general&numExperts=25'
    ) as analysts:
      return json.loads(analysts.read())

  def get_analyst_evaluations(self, analyst):
    name = analyst['name'].lower().replace(' ', '-')
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'.
      format(name)
    ) as analyst_stocks:
      return json.loads(analyst_stocks.read())

  def is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

  def get_recommendations(self, analyst):
    stock_evaluations = self.get_analyst_evaluations(analyst)
    self.recommendations_list += [stock['name'] for stock in stock_evaluations if self.is_recommended(stock)]

  def get_all_recommendations(self):
    analysts = self.get_analysts_info()
    for analyst in analysts:
      print('getting picks for {}'.format(analyst['name']))
      time.sleep(20) # don't accidentally DDOS them/hit rate limits
      self.get_recommendations(analyst)

  def count_recommendations(self):
    self.get_all_recommendations()
    print(Counter(self.recommendations_list))


scraper = TipRanksScraper()
scraper.count_recommendations()
