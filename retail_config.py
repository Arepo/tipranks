import pdb

from tabulator import Tabulator

class RetailConfig:

    def __init__(
        self,
        number_of_analysts=25,
        min_success_rate=0,
        min_stock_proportion=0,
        save_recommendations=False,
        tabulator=Tabulator()
    ):
        self.number_of_analysts = number_of_analysts
        self.min_success_rate = min_success_rate
        self.min_stock_proportion = min_stock_proportion
        self.save_recommendations = save_recommendations
        self.tabulator = tabulator

    def description(self):
        return f'Companies constituting at least a proportion of '\
               f'{self.min_stock_proportion} of the portfolio of the '\
               f'top {self.number_of_analysts} retail investors'

    def analysts_url(self):
        return ('https://www.tipranks.com/api/experts/getTop25Experts/'\
                f'?expertType=10&numExperts={self.number_of_analysts}')

    def stocks_url(self, analyst):
        return ('https://www.tipranks.com/api/publicportfolio/'\
                f'getportfoliobyid/?id={analyst["expertPortfolioId"]}')

    def filter_analysts(self, analysts):
        return [analyst for analyst in analysts
                if analyst['recommendations']['ratio'] > self.min_success_rate]

    def analyst_stock_picks(self, analyst):
        return analyst['allocation']['byCompany']

    def is_recommended(self, stock):
        return stock['percent'] > self.min_stock_proportion

    def get_stock_identity(self, stock):
        return stock['holdings'][0]['ticker'] + ' (' + stock['companyName'] + ')'

    def write_to_csv(self, analyst, stock_evaluations, date):
        csv_title = f'./past_data/retail_investors/retail_portfolios_for_'\
                    f'{date.today()}.csv'
        self.tabulator.write_to_retail_analyst_portfolios(analyst,
                                                          stock_evaluations,
                                                          csv_title)
