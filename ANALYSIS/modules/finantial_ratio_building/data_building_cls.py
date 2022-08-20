import numpy as np 
import pandas as pd


class FinanceRatiosBuilding: 
    
    def __init__(self, finance_data_route, parse_date):
        
        if parse_date != 'yes':
        
            self.raw_data = pd.DataFrame(pd.read_csv(finance_data_route))
            
        else:
            self.raw_data = pd.DataFrame(pd.read_csv(finance_data_route, parse_dates = ['Date']))\
                .set_index('Date')
                
    def PortfolioMarketCapitalization(self):
        
        
        # Finish defining the portfolio weights as a numpy array
        self.portfolio_weights = np.array([0.12, 0.15, 0.08, 0.05, 0.09, 0.10, 0.11, 0.14, 0.16])

        # Calculate the weighted stock returns
        WeightedReturns = self.raw_data.mul(self.portfolio_weights, axis=1)

        # Calculate the portfolio returns
        portfolio_data['Portfolio'] = WeightedReturns.sum(axis=1)
        
       #--------------- 
        
        
        # Create an array of market capitalizations (in billions)
        market_capitalizations = np.array([601.51, 469.25, 349.5, 310.48, 299.77, 356.94, 268.88, 331.57, 246.09])

        # Calculate the market cap weights
        mcap_weights = market_capitalizations / sum(market_capitalizations)

        # Calculate the market cap weighted portfolio returns
        self.portfolio_data['Portfolio_MCap'] = self.portfolio_data.iloc[:, 0:9].mul(mcap_weights, axis=1).sum(axis=1)
        
        
    def PortfolioVolatility(self):
        
        firms = self.raw_data.columns.to_list()
        
        # Calculate the covariance matrix
        cov_mat = self.portfolio_data.loc[:,firms].cov()

        # Annualize the co-variance matrix
        cov_mat_annual = cov_mat*252
        
        # Calculate the portfolio standard deviation
        self.portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(cov_mat_annual, portfolio_weights)))
        
        
        
        
        
        
        
        
                