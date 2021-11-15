import re
import yfinance as yf
from collections import Counter
import pdb

# This functions best if you have a lot of time on your hands

class CompaniesFilter:
  def __init__(self, companies: dict):
    self.companies = companies
    self.small_caps = []
    self.unknown_caps = []
    self.counted_small_caps = None
    self.counted_unknown_caps = None

  def filter_by_market_cap(self, max_market_cap=5000000000):
    # Only get those below the specified market cap
    for company_name in self.companies:
      self.__log_whether_smallcap(company_name, max_market_cap)

    self.counted_small_caps = Counter(
      {company_name:count for (company_name, count) in self.companies.items()
        if self.__tipranks_ticker(company_name) in self.small_caps}
    )
    self.counted_unknown_caps = Counter(
      {company_name:count for (company_name, count) in self.companies.items()
        if self.__tipranks_ticker(company_name) in self.unknown_caps}
    )

  def __log_whether_smallcap(self, company_name, max_market_cap):
    tipranks_ticker = self.__tipranks_ticker(company_name)
    market_cap = self.__market_cap(company_name)
    if market_cap < max_market_cap and market_cap > 0:
      print(company_name + ' has market cap of {}'.format(market_cap))
      self.small_caps.append(tipranks_ticker)
    elif market_cap == 0:
      print(company_name + ' has unknown market cap')
      self.unknown_caps.append(tipranks_ticker)
    else:
      print(company_name + ' has too high a market cap - discarded')

  def __market_cap(self, company_name):
    yf_ticker = self.__yf_ticker(company_name)
    company = yf.Ticker(yf_ticker).info
    if 'marketCap' in company.keys():
      return (company['marketCap'] or 0)
    else:
      return 0

  def __yf_ticker(self, company_name) -> str:
    return re.search('(\w+)', company_name).group(0)

  def __tipranks_ticker(self, company_name) -> str:
    return re.search('(\S+)', company_name).group(0)

