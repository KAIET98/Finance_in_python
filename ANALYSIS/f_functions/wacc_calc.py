
import numpy_financial as npf


class wacc_npv:
    
    def __init__(self, mval_debt, mval_equity, cost_equity, cost_debt, tax_rate):
        
        self.percent_debt = mval_debt/(mval_debt+mval_equity)

        self.percent_equity = mval_equity/(mval_debt+mval_equity)

        self.cost_equity  = cost_equity

        self.cost_debt = cost_debt

        self.tax_rate = tax_rate





        print('... you owe {} for the project, and you are holding extra {} for it ...'.format(mval_debt, mval_equity))
              
    def wacc_calc(self):
        self.wacc = self.percent_equity*self.cost_equity + self.percent_debt*self.cost_debt*(1-self.tax_rate)
              
        print(' ... WACC: {}'.format(self.wacc))
        
        return self.wacc
                
                
              
              
              
              
    
              
        
              
        
              
            