from analyst_scraper import AnalystScraper
from wall_st_config import WallStConfig
from retail_config import RetailConfig
from hedge_fund_config import HedgeFundConfig
from blogger_config import BloggerConfig

# scraper = AnalystScraper(RetailConfig(number_of_analysts=50))
# print(scraper.count_recommendations())

scraper = AnalystScraper(WallStConfig(number_of_analysts=3))
print(scraper.count_recommendations())

# scraper = AnalystScraper(HedgeFundConfig(number_of_analysts=50))
# print(scraper.count_recommendations())

# scraper = AnalystScraper(BloggerConfig(number_of_analysts=50))
# print(scraper.count_recommendations())


