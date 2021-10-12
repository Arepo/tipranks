from analyst_scraper import AnalystScraper
from wall_st_config import WallStConfig
from retail_config import RetailConfig
from hedge_fund_config import HedgeFundConfig
from blogger_config import BloggerConfig

scraper = AnalystScraper(RetailConfig(number_of_analysts=25, min_success_rate=0, min_stock_proportion=0.00))
print(scraper.count_recommendations())

# scraper = AnalystScraper(WallStConfig(number_of_analysts=50, sector='general'))
# print(scraper.count_recommendations())

# scraper = AnalystScraper(HedgeFundConfig(number_of_analysts=25, min_stock_proportion=0, max_market_cap=5000000000))
# print(scraper.count_recommendations())

# scraper = AnalystScraper(BloggerConfig(number_of_analysts=25))
# print(scraper.count_recommendations())


