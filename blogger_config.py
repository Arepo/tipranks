from tabulator import Tabulator
import pdb

class BloggerConfig:

  def __init__(self, number_of_analysts=25, save_recommendations=False, tabulator=Tabulator()):
    self.number_of_analysts = number_of_analysts
    self.save_recommendations = save_recommendations
    self.tabulator = tabulator

  def description(self):
    return f"Recommendations from top {self.number_of_analysts} financial bloggers"

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=blogger&period=year&benchmark=naive&numExperts={num}'
      .format(num=self.number_of_analysts))

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
    return stock['ticker'] + " (" + stock['name'] + ")"

  def write_to_csv(self, analyst, stock_evaluations, date):
    csv_title = f'./past_data/financial_bloggers_{date.today()}.csv'
    self.tabulator.write_to_analyst_csv(csv_title, analyst)
