from datetime import datetime
import pandas as pd
import numpy as np

def generate_random_data():

    date = pd.date_range(end = '2015-01-01', periods = 100).to_pydatetime().tolist()
    deliquency = np.random.randint(0, 100, size = 100)

    data = {'date' : date, 
                'Mortgage Delinquency Rate':deliquency}
    df = pd.DataFrame(data)\
    .set_index('date')

    return df