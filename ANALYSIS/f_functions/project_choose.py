
import numpy_financial as npf



class project_choose:
    
    def __init__(self, project_1_cf, project_2_cf):
        
        self.pr_1  = project_1_cf
        
        self.pr_2 = project_2_cf
    
    def irr_decision(self):
        
        irr1 = npf.irr(self.pr_1)
        
        irr2 = npf.irr(self.pr_2)
        
        if irr1>irr2: 
            
            return 1
        
        else: 
            
            return 2
    
    