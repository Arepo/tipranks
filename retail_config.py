from tabulator import Tabulator

class RetailConfig:

  def __init__(
    self,
    number_of_analysts=25,
    min_success_rate=0,
    min_stock_proportion=0,
    tabulator=Tabulator()
  ):
    self.number_of_analysts = number_of_analysts
    self.min_success_rate = min_success_rate
    self.min_stock_proportion = min_stock_proportion
    self.tabulator = tabulator

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
    return stock['percent'] > self.min_stock_proportion

  def get_stock_identity(self, stock):
    return stock['companyName'] + " (" + stock['holdings'][0]['ticker'] + ")"

  def write_to_csv(self, analyst, stock_evaluations):
    self.tabulator.write_to_retail_analyst_portfolios(analyst, stock_evaluations)
