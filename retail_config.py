class RetailConfig:

  def __init__(
    self,
    number_of_analysts=25,
    min_success_rate=0.8,
    stock_identifier='ticker',
    min_stock_percent=0.01
  ):
    self.number_of_analysts = number_of_analysts
    self.min_success_rate = min_success_rate
    self.stock_identifier = stock_identifier # Can also be 'companyName' for for readability,
                                             # though then can't filter by market cap
    self.min_stock_percent = min_stock_percent

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts={}'
      .format(self.number_of_analysts))

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id={}'
      .format(analyst['expertPortfolioId']))

  def filter_analysts(self, analysts):
    return [analyst for analyst in analysts if analyst['recommendations']['ratio'] > self.min_success_rate]

  def evaluations_from_analyst(self, analyst):
    return analyst['allocation']['byCompany']

  def is_recommended(self, stock):
    return stock['percent'] > self.min_stock_percent

  def get_stock_identity(self, stock):
    if self.stock_identifier == 'companyName':
      return stock[self.stock_identifier]
    else:
      return stock['holdings'][0]['ticker']
