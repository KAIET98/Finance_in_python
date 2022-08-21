import numpy as np
import pandas as pd
from scipy.stats import norm

from ..finantial_ratio_building.data_building_cls import FinanceRatiosBuilding


class RiskMeasurement(FinanceRatiosBuilding):


    def __init__(self):

        print(' ... clase cargada ...')


    def HistoricVaR(self):

        StockReturns_perc = cum_rets['USO']*100

        return StockReturns_perc


    

        

    def VaROverHistoricData(self):

        quantiles = [95,99,99.99]

        quantile_var = {}

        for q in quantiles: 

            error = 100 - q

            var_i = np.percentile(StockReturns_perc, error)


            quantile_var[q] = var_i

        return quantile_var

    
    def ConditionalValueAtRisk(self):


        conditional_var = {}

        for keys in quantile_var.keys().to_list():


            cvar_i = StockReturns_perc[StockReturns_perc <= var_95].mean()

            conditional_var[keys] = cvar_i


        return conditional_var


    def ParametricVaR(self):

        mu = np.mean(StockReturns)

        # Estimate the daily volatility
        vol = np.std(StockReturns)

        parametricVaR  = {}

        for confidence_level in quantile_var.keys().to_list():


            pVar_I = norm.ppf(100 - confidence_level, mu, vol)

            parametricVaR[confidence_level] = pVar_I


        return parametricVaR

    
    def MonteCarloSimulation(self):

        T = 252
        S0 = 10

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
        var_99 = np.percentile(sim_returns, 1)









        


