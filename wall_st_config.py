from tabulator import Tabulator
import pdb

class WallStConfig:

    def __init__(
        self,
        number_of_analysts=25,
        sector='general',
        min_success_rate=0,
        save_recommendations=False,
        tabulator=Tabulator()
    ):
        self.number_of_analysts = number_of_analysts
        self.sector = sector
        # Sector can be 'general', 'materials', 'services', 'healthcare',
        # 'financial', 'technology' and 'utilities'. Other strings
        # default to 'general'
        self.min_success_rate = min_success_rate
        self.save_recommendations = save_recommendations
        self.tabulator = tabulator

    def description(self):
        return f"Recommendations from top {self.number_of_analysts}"\
            f" Wall Street analysts in the {self.sector} sector"

    def analysts_url(self):
        return ('https://www.tipranks.com/api/experts/GetTop25Experts/'\
          '?expertType=analyst&period=year&benchmark=naive=2&sector='\
          f'{self.sector}&numExperts={self.number_of_analysts}')

    def stocks_url(self, analyst):
        return ('https://www.tipranks.com/api/experts/getStocks/?period'\
          '=year&benchmark=naive&name={}'
          .format(analyst['name'].lower().replace(' ', '-')))

    def filter_analysts(self, analysts):
        return [
          analyst for analyst in analysts if
          analyst['recommendations']['ratio'] > self.min_success_rate]

    def evaluations_from_analyst(self, analyst):
        return analyst

    def is_recommended(self, stock):
        return stock['latestRating']['rating'].lower() == 'buy'

    def get_stock_identity(self, stock):
        return stock['ticker'] + " (" + stock['name'] + ")"

    def write_to_csv(self, analyst, stock_evaluations, date):
        analyst_csv_title = f'./past_data/ws_analysts_{date.today()}.csv'
        self.tabulator.write_to_analyst_csv(analyst_csv_title, analyst)
        self.tabulator.write_to_analysts_companies(analyst,
                                                   stock_evaluations,
                                                   date)


