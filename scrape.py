from analyst_scraper import AnalystScraper
from wall_st_config import WallStConfig
from retail_config import RetailConfig
from hedge_fund_config import HedgeFundConfig
from blogger_config import BloggerConfig
from companies_filter import CompaniesFilter
import pdb

# scraper = AnalystScraper(RetailConfig(
#     number_of_analysts=25,
#     save_recommendations=False
# ))
# print(scraper.count_recommendations())

scraper = AnalystScraper(WallStConfig(
    number_of_analysts=25,
    save_recommendations=False,
    sector='services'

))
print(scraper.count_recommendations())

# scraper = AnalystScraper(HedgeFundConfig(
#     number_of_analysts=50,
#     save_recommendations=False
# ))
# print(scraper.count_recommendations())

# scraper = AnalystScraper(BloggerConfig(
#     number_of_analysts=2,
#     save_recommendations=False
# ))
# print(scraper.count_recommendations())


recommendations = scraper.aggregated_recommendations()
cfilter = CompaniesFilter(recommendations)
cfilter.filter_by_market_cap(max_market_cap=5000000000)
print(f"Small caps: {cfilter.small_caps}")
print(f"Unknown caps: {cfilter.unknown_caps}")
