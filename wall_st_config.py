class WallStConfig:

  def __init__(self, number_of_analysts=25, stock_identifier='name'):
    self.number_of_analysts = number_of_analysts
    self.stock_identifier = stock_identifier # Can also use 'ticker'

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'
      .format(analyst['name'].lower().replace(' ', '-')))

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general&numExperts={}'
      .format(self.number_of_analysts))

  def filter_analysts(self, analysts):
    return analysts

  def evaluations_from_analyst(self, analyst):
    return analyst

  def is_recommended(self, stock):
    return stock['latestRating']['rating'].lower() == 'buy'

