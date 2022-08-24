
import numpy as np
import pandas as pd


def portfolio_losses():
    
    date = pd.date_range(start = '2005-01-03', end = '2010-12-30', periods = 1510).to_pydatetime().tolist()
    deliquency = np.random.uniform(-0.34704482955933935, 0.19873408496120976, size = 1510)

    data = {'date' : date, 
                'Mortgage Delinquency Rate':deliquency}
    df = pd.DataFrame(data)\
    .set_index('date')

    return df