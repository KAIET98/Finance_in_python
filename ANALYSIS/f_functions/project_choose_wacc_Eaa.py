import numpy_financial as npf




class project_choose_wacc_eaa:
    
    def __init__(self, project_1_cf, project_2_cf, wacc, project_1_period, project_2_period):
        
        self.cf_project1  = project_1_cf
        
        self.cf_project2 = project_2_cf
        
        self.wacc  = wacc
        self.project_1_period = project_1_period
        self.project_2_period = project_2_period
        
        
        # IRR calculation 
        
        # Calculate the IRR for Project 1
        self.irr_project1 = npf.irr(self.cf_project1)
        

        # Calculate the IRR for Project 2
        self.irr_project2 = npf.irr(self.cf_project2)
        
        # NPV calculation 
        
        # Calculate the NPV for Project 1
        self.npv_project1 = npf.npv(rate = wacc, values = self.cf_project1)
        

        # Calculate the NPV for Project 2
        self.npv_project2 = npf.npv(rate = wacc, values = self.cf_project2)
        
        
    
    def eaa_decision(self):
        
        # Calculate the EAA for Project 1
        eaa_project1 = npf.pmt(rate=self.wacc, nper=self.project_1_period, pv=-1*self.npv_project1, fv=0)
       

        # Calculate the EAA for Project 2
        eaa_project2 = npf.pmt(rate=self.wacc, nper=self.project_2_period, pv=-1*self.npv_project2, fv=0)
        
        
        
        print("Project 1 IRR: " + str(round(100*self.irr_project1, 2)) + "%")
        print("Project 1 NPV: " + str(round(self.npv_project1, 2)))
        print("Project 1 EAA: " + str(round(eaa_project1, 2)))
        
        print("Project 2 IRR: " + str(round(100*self.irr_project2, 2)) + "%")
        print("Project 2 NPV: " + str(round(self.npv_project2, 2)))
        print("Project 2 EAA: " + str(round(eaa_project2, 2)))
        
        if eaa_project1 > eaa_project2 : 
            
            return 1
        
        else: 
            
            return 2