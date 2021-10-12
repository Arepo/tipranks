import csv
from datetime import date
import pdb

class Tabulator:
  def write_to_retail_analyst_portfolios(self, analyst, portfolio):
    csv_title = f'./past_data/portfolios_for_{date.today()}.csv'

    with open(csv_title, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      row = [analyst['expertPortfolioId'], analyst['name']]

      row.extend([
        '{name} ({ticker}): {portfolio_percent}'.format(
          name=company['companyName'],
          ticker=company['holdings'][0]['ticker'],
          portfolio_percent=company['percent']
        ) for company in portfolio])
      writer.writerow(row)

