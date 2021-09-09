import yfinance as yf

# This function best if you have a lot of time on your hands

def filter_by_market_cap(recommendations, max_market_cap=5000000000):
    # Only get those below the specified market cap
    unique_values = list(dict.fromkeys(recommendations)) # This won't work in pdb - see https://stackoverflow.com/a/23050282/3210927
    small_caps = []
    no_caps = []
    for ticker in unique_values:
      company = yf.Ticker(ticker).info

      if 'marketCap' in company.keys():
        market_cap = (company['marketCap'] or 0)
      else:
        market_cap = 0

      if 'shortName' in company.keys() and company['shortName']:
        name = company['shortName']
      else:
        name = ticker
      # print(company)
      if market_cap < max_market_cap and market_cap > 0:
        print(name + ' has market cap of {}'.format(market_cap))
        small_caps.append(ticker)
      elif market_cap == 0:
        print(name + ' has unknown market cap')
        no_caps.append(ticker)
      else:
        print(name + ' has too high a market cap - discarded')


    print(
      'small caps are {}'.format(
      {ticker:count for (ticker, count) in recommendations.items() if ticker in small_caps}
    ))

    print(
      'Caps unknown for {}'.format(
      {ticker:count for (ticker, count) in recommendations.items() if ticker in no_caps}
    ))
