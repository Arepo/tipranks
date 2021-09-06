class WallStConfig:

  def __init__(self, number_of_analysts=25, stock_identifier='name'):
    self.number_of_analysts = number_of_analysts
    self.stock_identifier = stock_identifier

  # def count_recommendations(self):
  #   return self.thing_doer.count_recommendations()

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

  # def __get_analysts_info(self):
  #   if self.analysts_info is not None:
  #     return self.analysts_info

  #   with urllib.request.urlopen(
  #     'https://www.tipranks.com/api/experts/GetTop25Experts/?expertType=analyst&period=year&benchmark=naive&sector=general&numExperts={}'
  #       .format(self.number_of_analysts)
  #   ) as analysts:
  #     self.analysts_info = json.loads(analysts.read())
  #     return self.analysts_info

  # def __get_analyst_evaluations(self, analyst):
  #   name = analyst['name'].lower().replace(' ', '-')
  #   with urllib.request.urlopen(
  #     'https://www.tipranks.com/api/experts/getStocks/?period=year&benchmark=naive&name={}'.
  #     format(name)
  #   ) as analyst_stocks:
  #     return json.loads(analyst_stocks.read())

  # def __is_recommended(self, stock):
  #   return stock['latestRating']['rating'].lower() == 'buy'

  # # def __get_recommendations(self, analyst):
  # #   stock_evaluations = self.__get_analyst_evaluations(analyst)
  # #   self.recommendations_list += [stock['name'] for stock in stock_evaluations if self.__is_recommended(stock)]

  # def __get_filtered_recommendations(self):
  #   for analyst in self.__get_analysts_info():
  #     print('getting picks for {}'.format(analyst['name']))
  #     time.sleep(3) # don't accidentally DDOS them/hit rate limits
  #     self.__get_recommendations(analyst)




# scraper = WallStScraper()
# scraper.count_recommendations()

