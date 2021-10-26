from .analyst_scraper import AnalystScraper
from .wall_st_config import WallStConfig
from .retail_config import RetailConfig
from .hedge_fund_config import HedgeFundConfig
from .blogger_config import BloggerConfig
import pdb

# Fix tests before making changes, since the API might have changed from under us
# and the data almost certainly will have

def test_retail_scraping():
  scraper = AnalystScraper(RetailConfig(
    number_of_analysts=4,
    min_stock_proportion=0.01,
    min_success_rate=0.5
  ))
  assert scraper.count_recommendations()['NVAX'] == 1

# def test_wall_st_scraping():
#   scraper = AnalystScraper(WallStConfig(
#     number_of_analysts=1,
#     sector='general'
#   ))
#   assert scraper.count_recommendations()['Analog Devices (ADI)'] == 1

# def test_hedge_fund_scraping():
#   scraper = AnalystScraper(HedgeFundConfig(
#     number_of_analysts=1,
#     min_stock_proportion=0.05,
#     max_market_cap=0
#   ))
#   assert scraper.count_recommendations()['Amazon (AMZN)'] == 1

# def test_blogger_scraping():
#   scraper = AnalystScraper(BloggerConfig(
#     number_of_analysts=1,
#   ))
#   assert scraper.count_recommendations()['Cloudera (CLDR)'] == 1
