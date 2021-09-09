from .analyst_scraper import AnalystScraper
from .wall_st_config import WallStConfig
from .retail_config import RetailConfig
import pdb

# Run tests before making changes, since the API might have changed from under us
# and the data almost certainly will have

def test_retail_scraper():
    scraper = AnalystScraper(RetailConfig(
        number_of_analysts=4,
        stock_identifier='ticker',
        min_stock_percent=0.01,
        min_success_rate=0.8
    ))
    assert scraper.count_recommendations()['NVAX'] == 1

def test_wall_st_scraper():
    scraper = AnalystScraper(WallStConfig(number_of_analysts=1))
    assert scraper.count_recommendations()['DOCU'] == 1
