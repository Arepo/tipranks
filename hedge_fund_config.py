import pdb

class HedgeFundConfig:
  def __init__(
    self,
    number_of_analysts=25,
    stock_identifier='name',
    min_stock_percent=0.05,
    max_market_cap=5000000000
  ):
    self.number_of_analysts = number_of_analysts
    self.stock_identifier = stock_identifier # Can also use 'ticker'
    # pdb.set_trace()
    self.min_stock_percent = min_stock_percent
    self.max_market_cap = max_market_cap

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/hedgeFunds/getInfo/{}/'
      .format(analyst['name'].lower().replace(' ', '-')))

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=institutional&period=year&benchmark=naive&sector=general'
      .format(self.number_of_analysts))

  def filter_analysts(self, analysts):
    return analysts

  def evaluations_from_analyst(self, analyst):
    return analyst['activities']['quarter']

  def is_recommended(self, stock):
    if (int(stock['marketCap'] or 0) < self.max_market_cap and
      stock['portfolioPercent']    > self.min_stock_percent):
      return True
    return False

