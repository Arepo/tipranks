import csv
import os.path
import pdb

class Tabulator:
  # def write_to_analysts_companies(self, analyst, stock_evaluations):


  def write_to_retail_analyst_portfolios(self, analyst, portfolio):
    csv_title = f'./past_data/retail_portfolios_for_{date.today()}.csv'

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


  def write_to_analyst_csv(self, csv_title, analyst):
    # Move id and name to the left
    analyst_keys = list(analyst.keys())
    analyst_keys.remove('expertId')
    analyst_keys.remove('name')
    headers = ['expertId', 'name']
    headers.extend(analyst_keys)
    file_exists = os.path.isfile(csv_title)

    with open(csv_title, 'a', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

      if not file_exists:
        writer.writeheader()
      # row = [analyst[key] for key in headers]
      row = { key:analyst[key] for key in headers }
      # pdb.set_trace()
      writer.writerow(row)

