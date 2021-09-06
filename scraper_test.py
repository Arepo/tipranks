from .wall_st_scraper import WallStScraper
from .retail_scraper import RetailScraper

# def test_retail_scraper():
#     scraper = RetailScraper(number_of_analysts=4)
#     assert scraper.count_recommendations()['Novavax'] == 1

def test_wall_st_scraper():
    scraper = WallStScraper(number_of_analysts=1)
    assert scraper.count_recommendations()['DocuSign'] == 1
