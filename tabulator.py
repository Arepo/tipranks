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

  def write_to_wall_street_analysts(self, analyst, companies):
    csv_title = f'./past_data/ws_analysts_for_{date.today()}.csv'
    # pdb.set_trace()
    with open(csv_title, 'a', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      row = [
        analyst['expertId'],
        analyst['name'],
        analyst['distribution'],
        analyst['recommendations'],
        analyst['rank'],
        analyst['averageReturn'],
        analyst['firm'],
        analyst['sectorId'],
        analyst['uid'],
        analyst['numUsersSubscribedToExpert'],
        analyst['hedgeFundValue'],
        analyst['hedgeFundName'],
        analyst['insiderCompanyName'],
        analyst['expertType'],
        analyst['expertPortfolioId'],
        analyst['portfolioPerformanceScores'],
        analyst['isFollowing'],
        analyst['portfolioRisk'],
        analyst['sectorIdEnum'],
        analyst['holdingsCount'],
        analyst['expertTypeIdEnum'],
        analyst['portfolioName'],
        analyst['followedSince'],
        analyst['ratings'],
        analyst['expertUrlSuffix'],
        analyst['portfolioRiskEnum'],
        analyst['portfolioBeta']
      ]
      writer.writerow(row)


