import numpy as np
import pandas as pd
from scipy.stats import norm

from ..finantial_ratio_building.data_building_cls import FinanceRatiosBuilding


class RiskMeasurement(FinanceRatiosBuilding):


    def __init__(self):

        print(' ... importing financial data ...')

        print(



            '''
            For MonteCarloSimulation method, please indicate a 'd' to choose the first historic price for the indicated firm, otherwise
            it is going to pick a default 10 to simulate
            
            
            
            
            '''
        )


        data_route = 'https://assets.datacamp.com/production/repositories/1546/datasets/fb7165b7270a3721f69abf9ff09b85938d9d1068/Big9Returns2017.csv'


        FRB = FinanceRatiosBuilding(finance_data_route= data_route, 
                                    parse_date= 'yes', 
                                    risk_free_rate = 0)


        FRB.PortfolioMarketCapitalization()


        FRB.PortfolioVolatility()


        FRB.SharpeRatio()

        FRB.MSR_Portfolio()


        self.finance_data = FRB.GMV()

        print(self.finance_data.head())



    def HistoricVaR(self, column):

        self.column = column

        self.firm_historic_VaR = self.finance_data[self.column]*100

        return self.firm_historic_VaR


    

        

    def VaROverHistoricData(self):

        quantiles = [95,99,99.99]

        self.quantile_var = {}

        for q in quantiles: 

            error = 100 - q

            var_i = np.percentile(self.firm_historic_VaR, error)


            self.quantile_var[q] = var_i

        return self.quantile_var

    
    def ConditionalValueAtRisk(self):


        


        conditional_var = {}

        

        for keys in list(self.quantile_var.keys()):

            var_i = self.quantile_var[keys]


            cvar_i = self.firm_historic_VaR[self.firm_historic_VaR <= var_i].mean()

            conditional_var[keys] = cvar_i


        return conditional_var


    def ParametricVaR(self):

        mu = np.mean(self.firm_historic_VaR)

        # Estimate the daily volatility
        vol = np.std(self.firm_historic_VaR)

        parametricVaR  = {}

        for confidence_level in list(self.quantile_var.keys()):


            pVar_I = norm.ppf(100 - confidence_level, mu, vol)

            parametricVaR[confidence_level] = pVar_I


        return parametricVaR

    
    def MonteCarloSimulation(self, days, initial_price):

        if initial_price == 'd':

            S0 = self.finance_data[self.column].iloc[0]

        else: 

            S0 = 10

        



        T = days
        #S0 = 10

        mu = np.mean(self.finance_data[self.column])
        vol = np.std(self.finance_data[self.column])

        # Add one to the random returns
        rand_rets = np.random.normal(mu, vol, T) + 1

        # Aggregate the returns
        sim_returns = []

        # Loop through 100 simulations
        for i in range(100):

            # Generate the Random Walk
            rand_rets = np.random.normal(mu, vol, T)
            
            # Save the results
            sim_returns.append(rand_rets)

        # Calculate the VaR(99)
        var_99_firm_i = np.percentile(sim_returns, 1)

        print("Parametric VaR(99): ", round(100*var_99_firm_i, 2),"%")

        print('En el peor {} % de los casos las perdidas no superaran el {} % '.format(1,var_99_firm_i * 100 ))

        return var_99_firm_i









        


