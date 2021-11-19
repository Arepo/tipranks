from tabulator import Tabulator
import pdb

class HedgeFundConfig:

  def __init__(
    self,
    number_of_analysts=25,
    min_stock_proportion=0,
    max_market_cap=0000000000,
    save_recommendations=False,
    tabulator=Tabulator()
  ):
    self.number_of_analysts = number_of_analysts
    self.min_stock_proportion = min_stock_proportion
    self.max_market_cap = max_market_cap
    self.save_recommendations = save_recommendations
    self.tabulator = tabulator
    self.description = 'hedge funds'

  def description(self):
    return (
      'Companies constituting at least a proportion of '\
      f'{self.min_stock_proportion} of the portfolio of the top '\
      f'{self.number_of_analysts} hedge funds')

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/hedgeFunds/getInfo/{}/'
      .format(analyst['name'].lower().replace(' ', '-')))

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/'\
      '?expertType=institutional&period=year&benchmark=naive&sector='\
      'general&numExperts={self.number_of_analysts}')

  def filter_analysts(self, analysts):
    return analysts

  def analyst_stock_picks(self, analyst):
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
    return stock['ticker'] + ' (' + stock['name'] + ')'

  def write_to_csv(self, analyst, stock_evaluations, date):
    csv_title = f'./past_data/hedge_funds/hedge_fund_analysts_{date.today()}.csv'
    self.tabulator.write_to_analyst_csv(csv_title, analyst)
