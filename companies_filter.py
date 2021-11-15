import re
import yfinance as yf
from collections import Counter
import pdb

# This functions best if you have a lot of time on your hands

class CompaniesFilter:
  def __init__(self, companies: dict):
    self.companies = companies

  def filter_by_market_cap(self, max_market_cap=5000000000):
    # Only get those below the specified market cap

    small_caps = []
    no_caps = []
    companies = self.companies
    for company_name in list(self.companies.keys()):
      yf_ticker = self.__yf_ticker(company_name)
      company = yf.Ticker(yf_ticker).info
      tipranks_ticker = self.__tipranks_ticker(company_name)

      if 'marketCap' in company.keys():
        market_cap = (company['marketCap'] or 0)
      else:
        market_cap = 0

      if 'shortName' in company.keys() and company['shortName']:
        name = company['shortName']
      else:
        name = tipranks_ticker

      if market_cap < max_market_cap and market_cap > 0:
        print(name + ' has market cap of {}'.format(market_cap))
        small_caps.append(tipranks_ticker)
      elif market_cap == 0:
        print(name + ' has unknown market cap')
        no_caps.append(tipranks_ticker)
      else:
        print(name + ' has too high a market cap - discarded')
    self.small_caps = Counter({company_name:count for (company_name, count) in self.companies.items() if self.__tipranks_ticker(company_name) in small_caps})

    self.unknown_caps = Counter({company_name:count for (company_name, count) in self.companies.items() if self.__tipranks_ticker(company_name) in no_caps})

  def __yf_ticker(self, company_name) -> str:
    return re.search('(\w+)', company_name).group(0)

  def __tipranks_ticker(self, company_name) -> str:
    return re.search('(\S+)', company_name).group(0)
