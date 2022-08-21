import numpy as np
import pandas as pd

class cap2_data:
    
    def __init__(self, ruta_cap_data, ruta_stock_returnm, risk_free, numstocks):
        
        self.cap_data = pd.read_csv(ruta_cap_data)
        self.risk_free = risk_free
        self.stock_data = pd.read_csv(ruta_stock_returnm, parse_dates = ['Date'])\
.set_index('Date')
        
        self.numstocks = numstocks 
        
    
        
    def portfolio_return(self): 
        
        # Finish defining the portfolio weights as a numpy array
        portfolio_weights = np.array([0.12, 0.15, 0.08, 0.05, 0.09, 0.10, 0.11, 0.14, 0.16])

        # Calculate the weighted stock returns
        WeightedReturns = self.stock_data.mul(portfolio_weights, axis=1)

        # Calculate the portfolio returns
        self.stock_data['Portfolio'] = WeightedReturns.sum(axis=1)

        return self.stock_data
    
    
    def portfolio_equally_return(self):
        
        # How many stocks are in your portfolio?
        #numstocks = 9

        # Create an array of equal weights across all assets
        portfolio_weights_ew = np.repeat(1/self.numstocks, self.numstocks)

        # Calculate the equally-weighted portfolio returns
        self.stock_data['Portfolio_EW'] = self.stock_data.iloc[:, 0:self.numstocks].mul(portfolio_weights_ew, axis=1).sum(axis=1)
        
        return self.stock_data
    
    def market_cap_portfol(self):
        
        # Create an array of market capitalizations (in billions)
        market_capitalizations = np.array([601.51, 469.25, 349.5, 310.48, 299.77, 356.94, 268.88, 331.57, 246.09])

        # Calculate the market cap weights
        mcap_weights = market_capitalizations / sum(market_capitalizations)

        # Calculate the market cap weighted portfolio returns
        self.stock_data['Portfolio_MCap'] = self.stock_data.iloc[:, 0:9].mul(mcap_weights, axis=1).sum(axis=1)
        
        return self.stock_data
        
        

        
    def sharpe(self): 
        
        self.cap_data['Sharpe'] = (self.cap_data['Returns'] - self.risk_free) / self.cap_data['Volatility']
        
        return self.cap_data
    
    
    def MSR(self):
        
        # Sort the portfolios by Sharpe ratio
        sorted_portfolios = self.cap_data.sort_values(by=['Sharpe'], ascending=False)

        # Extract the corresponding weights
        MSR_weights = sorted_portfolios.iloc[0, 0:self.numstocks]

        # Cast the MSR weights as a numpy array
        MSR_weights_array = np.array(MSR_weights)

        # Calculate the MSR portfolio returns
        self.stock_data['Portfolio_MSR'] = self.stock_data.iloc[:, 0:self.numstocks].mul(MSR_weights_array, axis=1).sum(axis=1)
        
        return self.stock_data
    
    
    def GMV(self):
        
        # Sort the portfolios by volatility
        sorted_portfolios = self.cap_data.sort_values(by=['Volatility'], ascending=True)

        # Extract the corresponding weights
        GMV_weights = sorted_portfolios.iloc[0,0:self.numstocks]

        # Cast the GMV weights as a numpy array
        GMV_weights_array = np.array(GMV_weights)

        # Calculate the GMV portfolio returns
        self.stock_data['Portfolio_GMV'] = self.stock_data.iloc[:, 0:self.numstocks].mul(GMV_weights_array, axis=1).sum(axis=1)
        
        return self.stock_data
    
    def RF(self):
        
        self.stock_data['RF'] = self.risk_free
        
        return self.stock_data
        
        

        
        

        
        

    
    
        
    