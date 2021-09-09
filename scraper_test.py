from .analyst_scraper import AnalystScraper
from .wall_st_config import WallStConfig
from .retail_config import RetailConfig
from .hedge_fund_config import HedgeFundConfig
import pdb

# Fix tests before making changes, since the API might have changed from under us
# and the data almost certainly will have

def test_retail_scraping():
  scraper = AnalystScraper(RetailConfig(
    number_of_analysts=4,
    stock_identifier='ticker',
    min_stock_percent=0.01,
    min_success_rate=0.8
  ))
  assert scraper.count_recommendations()['NVAX'] == 1

def test_wall_st_scraping():
  scraper = AnalystScraper(WallStConfig(
    number_of_analysts=1,
    stock_identifier='ticker',
    sector='general'
  ))
  assert scraper.count_recommendations()['DOCU'] == 1

def test_hedge_fund_scraping():
  scraper = AnalystScraper(HedgeFundConfig(
    number_of_analysts=1,
    stock_identifier='name',
    min_stock_percent=0.05,
    max_market_cap=0
  ))
  assert scraper.count_recommendations()['Amazon'] == 1
