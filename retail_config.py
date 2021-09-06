import pdb

class RetailConfig:

  def __init__(self, thing_doer=None, number_of_analysts=100, min_success_rate=0.8, stock_identifier='companyName'):
    self.number_of_analysts = number_of_analysts
    self.min_success_rate = min_success_rate
    self.stock_identifier = stock_identifier
    # self.number_of_analysts = number_of_analysts
    # if not thing_doer:
    #   self.thing_doer = ThingDoer(
    #     analysts_url='https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts={}'
    #     .format(number_of_analysts),
    #     filter_function=self.get_good_analysts_info)

  def stocks_url(self, analyst):
    return ('https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id={}'
      .format(analyst['expertPortfolioId']))

  def analysts_url(self):
    return ('https://www.tipranks.com/api/experts/getTop25Experts/?expertType=10&numExperts={}'
      .format(self.number_of_analysts))

  def filter_analysts(self, analysts):
    return [analyst for analyst in analysts if analyst['recommendations']['ratio'] > self.min_success_rate]

  def evaluations_from_analyst(self, analyst):
    return analyst['allocation']['byCompany']

  def is_recommended(self, stock):
    return stock['percent'] > 0.01

  # def count_recommendations(self):
  #   return self.thing_doer.count_recommendations()

  # def __get_analysts_info(self):
  #   if self.analysts_info is not None:
  #     return self.analysts_info

  #   with urllib.request.urlopen(
  #   ) as analysts:
  #     self.analysts_info = json.loads(analysts.read())
  #     return self.analysts_info

  # def get_good_analysts_info(self, analysts, min_success_rate=0.8):
  #   [analyst for analyst in analysts if analyst['recommendations']['ratio'] > min_success_rate]

  # def __get_analyst_evaluations(self, analyst):
  #   with urllib.request.urlopen(
  #     'https://www.tipranks.com/api/publicportfolio/getportfoliobyid/?id={}'.
  #     format(analyst['expertPortfolioId'])
  #   ) as analyst_stocks:
  #     return json.loads(analyst_stocks.read())['allocation']['byCompany']

  # def __get_recommendations(self, analyst):
  #   stock_holdings = self.__get_analyst_evaluations(analyst)
  #   self.recommendations_list += [stock['companyName'] for stock in stock_holdings if stock['percent'] > 0.01]

  # def __get_filtered_recommendations(self):
  #   for analyst in self.__get_good_analysts_info():
  #     print('getting picks for {}'.format(analyst['name']))
  #     time.sleep(3) # don't accidentally DDOS them/hit rate limits
  #     self.__get_recommendations(analyst)




# scraper = RetailScraper()
# scraper.count_recommendations()
