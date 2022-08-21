
from modules.finantial_ratio_building.data_building_cls import FinanceRatiosBuilding



def GetFinanceRatios(FinanceRatiosBuilding, finance_data_route, parse_date_option, risk_free_rate_absolute):
    FRB = FinanceRatiosBuilding(finance_data_route= finance_data_route, 
                                parse_date= parse_date_option, 
                                risk_free_rate = risk_free_rate_absolute)


    FRB.PortfolioMarketCapitalization()


    FRB.PortfolioVolatility()


    FRB.SharpeRatio()

    FRB.MSR_Portfolio()


    data = FRB.GMV()

    return data