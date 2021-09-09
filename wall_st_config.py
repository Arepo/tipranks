import yfinance as yf
import pdb

class WallStConfig:

  def __init__(self, number_of_analysts=25, stock_identifier='ticker', sector='general'):
    self.number_of_analysts = number_of_analysts
    self.stock_identifier = stock_identifier # Can also use 'name' for readability,
                                             # though then can't filter by market cap
    self.sector = sector # 'materials', 'services', 'healthcare', 'financial' and 'utilities' work. If it fails it defaults to 'general'

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive=2&sector={sector}&numExperts={num}'
      .format(sector=self.sector,num=self.number_of_analysts))


  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'
      .format(analyst['name'].lower().replace(' ', '-')))

  def filter_analysts(self, analysts):
    return analysts

  def evaluations_from_analyst(self, analyst):
    return analyst

  def is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

  def get_stock_identity(self, stock):
    return stock[self.stock_identifier]
