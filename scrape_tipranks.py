import urllib.request
import json
import pdb

class TipRanksScraper:

  def get_analysts_info(self):
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general'
    ) as analysts:
      return json.loads(analysts.read())

  def analyst_stocks_url(self, analyst):
    name = analyst['name'].lower().replace(' ', '-')
    with urllib.request.urlopen(
      'https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'.
      format(name)
    ) as analyst_stocks:
      return json.loads(analyst_stocks.read())

  def is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

  def extract_analyst_urls(self):
    analysts = self.get_analysts_info()
    stock_evaluations = self.analyst_stocks_url(analysts[0])
    recommendations = tuple(filter(self.is_recommended, stock_evaluations))
    print(tuple(map(lambda stock : stock['name'], recommendations)))




scraper = TipRanksScraper()
scraper.extract_analyst_urls()

