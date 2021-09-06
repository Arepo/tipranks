from .analyst_scraper import AnalystScraper
from .wall_st_config import WallStConfig
from .retail_config import RetailConfig

def test_retail_scraper():
    scraper = AnalystScraper(RetailConfig(number_of_analysts=4))
    assert scraper.count_recommendations()['Novavax'] == 1

# def test_wall_st_scraper():
#     scraper = AnalystScraper(WallStConfig(number_of_analysts=1))
#     assert scraper.count_recommendations()['DocuSign'] == 1
