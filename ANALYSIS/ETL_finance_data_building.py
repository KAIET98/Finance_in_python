
from modules.finantial_ratio_building.data_building_cls import FinanceRatiosBuilding

data_route = 'https://assets.datacamp.com/production/repositories/1546/datasets/fb7165b7270a3721f69abf9ff09b85938d9d1068/Big9Returns2017.csv'


FRB = FinanceRatiosBuilding(finance_data_route= data_route, 
                            parse_date= 'yes', 
                            risk_free_rate = 0)


FRB.PortfolioMarketCapitalization()


FRB.PortfolioVolatility()


FRB.SharpeRatio()

FRB.MSR_Portfolio()


data = FRB.GMV()

    
print(data)