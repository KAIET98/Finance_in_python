

import numpy_financial as npf



class project_choose_wacc_s:
    
    def __init__(self, project_1_cf, project_2_cf, wacc):
        
        self.cf_project1  = project_1_cf
        
        self.cf_project2 = project_2_cf
        
        self.wacc  = wacc
    
    def npv_decision(self):
        
        npv_project1 = npf.npv(rate = self.wacc, values = self.cf_project1)
        
        npv_project2 = npf.npv(rate = self.wacc, values = self.cf_project2)
        
        if npv_project1>npv_project2: 
            
            return 1
        
        else: 
            
            return 2