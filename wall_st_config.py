from tabulator import Tabulator
import pdb

class WallStConfig:

  def __init__(
    self,
    number_of_analysts=25,
    sector='general',
    min_success_rate=0,
    tabulator=Tabulator()
  ):
    self.number_of_analysts = number_of_analysts
                                             # though then can't filter by market cap
    self.sector = sector # 'materials', 'services', 'healthcare', 'financial', 'technology' and 'utilities' work. If it fails it defaults to 'general'
    self.min_success_rate = min_success_rate
    self.tabulator = tabulator

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive=2&sector={sector}&numExperts={num}'
      .format(sector=self.sector,num=self.number_of_analysts))


  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'
      .format(analyst['name'].lower().replace(' ', '-')))

  def filter_analysts(self, analysts):
    return [analyst for analyst in analysts if analyst['recommendations']['ratio'] > self.min_success_rate]

  def evaluations_from_analyst(self, analyst):
    return analyst

  def is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

  def get_stock_identity(self, stock):
    return stock['name'] + " (" + stock['ticker'] + ")"

  def write_to_csv(self, analyst, stock_evaluations, date):
    csv_title = f'./past_data/ws_analysts_{date.today()}.csv'
    self.tabulator.write_to_analyst_csv(csv_title, analyst)
    # self.tabulator.write_to_analysts_companies(analyst, stock_evaluations)


