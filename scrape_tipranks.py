import urllib.request

class TipRanksScraper:

  def __init__(self):
    print('hello world')


  def get_analysts(self):
    with urllib.request.urlopen('https://www.tipranks.com/analysts/top') as response:
      html = response.read()
    print(html)


scraper = TipRanksScraper()
scraper.get_analysts()
