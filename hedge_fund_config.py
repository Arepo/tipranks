import pdb

class HedgeFundConfig:

  def __init__(
    self,
    number_of_analysts=25,
    min_stock_proportion=0.05,
    max_market_cap=5000000000
  ):
    self.number_of_analysts = number_of_analysts
    self.min_stock_proportion = min_stock_proportion
    self.max_market_cap = max_market_cap

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/hedgeFunds/getInfo/{}/'
      .format(analyst['name'].lower().replace(' ', '-')))

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=institutional&period=year&benchmark=naive&sector=general&numExperts={}'
      .format(self.number_of_analysts))

  def filter_analysts(self, analysts):
    return analysts

  def evaluations_from_analyst(self, analyst):
    return analyst['activities']['quarter']

  def is_recommended(self, stock):
    market_cap = (int(stock['marketCap'] or 0))
    if (
      self.max_market_cap == 0 or
      market_cap < self.max_market_cap
    ) and (
      stock['portfolioPercent'] > self.min_stock_proportion
    ):
      return True
    return False

  def get_stock_identity(self, stock):
    return stock['name'] + " (" + stock['ticker'] + ")"
