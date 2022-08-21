import numpy as np 
import pandas as pd


class FinanceRatiosBuilding: 
    
    def __init__(self, finance_data_route, parse_date, risk_free_rate = 0):
        
        if parse_date != 'yes':
        
            self.raw_data = pd.DataFrame(pd.read_csv(finance_data_route))
            
        else:
            self.raw_data = pd.DataFrame(pd.read_csv(finance_data_route, parse_dates = ['Date']))\
                .set_index('Date')
            
            
        self.RF = risk_free_rate
                
    def PortfolioMarketCapitalization(self):
        
        
        # Finish defining the portfolio weights as a numpy array
        self.portfolio_weights = np.array([0.12, 0.15, 0.08, 0.05, 0.09, 0.10, 0.11, 0.14, 0.16])

        # Calculate the weighted stock returns
        WeightedReturns = self.raw_data.mul(self.portfolio_weights, axis=1)

        # Calculate the portfolio returns
        WeightedReturns['Portfolio'] = WeightedReturns.sum(axis=1)
        
       #--------------- 
        
        
        # Create an array of market capitalizations (in billions)
        self.market_capitalizations = np.array([601.51, 469.25, 349.5, 310.48, 299.77, 356.94, 268.88, 331.57, 246.09])

        # Calculate the market cap weights
        mcap_weights = self.market_capitalizations / sum(self.market_capitalizations)

        # Calculate the market cap weighted portfolio returns
        WeightedReturns['Portfolio_MCap_return'] = WeightedReturns.iloc[:, 0:9].mul(mcap_weights, axis=1).sum(axis=1)
        
        self.portfolio_data = WeightedReturns
        
        return self.portfolio_data
        
        
    def PortfolioVolatility(self):
        
        firms = self.raw_data.columns.to_list()
        
        # Calculate the covariance matrix
        cov_mat = self.portfolio_data.loc[:,firms].cov()

        # Annualize the co-variance matrix
        cov_mat_annual = cov_mat*252
        
        # Calculate the portfolio standard deviation
        self.portfolio_volatility = np.sqrt(np.dot(self.portfolio_weights.T, np.dot(cov_mat_annual, self.portfolio_weights)))
        
        #------PRUEBA----
        
        #Adjuntamos el dato de la volatilidad al dataframe global, 
        #esto no estaba previsto igual puede causar algunas desviaciones gordas
        
        self.portfolio_data['Volatility'] = self.portfolio_volatility
        
        
        
        return self.portfolio_volatility
    
    
    def SharpeRatio(self):
        
        self.portfolio_data['Sharpe'] = (self.portfolio_data['Portfolio_MCap_return'] - self.RF) / self.portfolio_data['Volatility']
        
        
        #formula original: 
        
        '''
        
        RandomPortfolios['Sharpe'] = (RandomPortfolios['Returns'] - risk_free) / RandomPortfolios['Volatility']

        
        '''
        
        
        
        return self.portfolio_data

    
    def MSR_Portfolio(self):
        
        self.numstocks = len(self.market_capitalizations)
        
        
        # Sort the portfolios by Sharpe ratio
        sorted_portfolios = self.portfolio_data.sort_values(by=['Sharpe'], ascending=False)

        # Extract the corresponding weights
        MSR_weights = sorted_portfolios.iloc[0, 0:self.numstocks]

        # Cast the MSR weights as a numpy array
        MSR_weights_array = np.array(MSR_weights)

        # Calculate the MSR portfolio returns
        
        self.portfolio_data['Portfolio_MSR'] = self.portfolio_data.iloc[:, 0:self.numstocks].mul(MSR_weights_array, axis=1).sum(axis=1)
        
        
        return self.portfolio_data
    
    
    def GMV(self):
        
        # Sort the portfolios by volatility
        sorted_portfolios = self.portfolio_data.sort_values(by=['Volatility'], ascending=True)

        # Extract the corresponding weights
        GMV_weights = sorted_portfolios.iloc[0,0:self.numstocks]

        # Cast the GMV weights as a numpy array
        GMV_weights_array = np.array(GMV_weights)

        # Calculate the GMV portfolio returns
        self.portfolio_data['Portfolio_GMV'] = self.portfolio_data.iloc[:, 0:self.numstocks].mul(GMV_weights_array, axis=1).sum(axis=1)
        
        return self.portfolio_data
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                