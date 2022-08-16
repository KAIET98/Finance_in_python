

def growth_depr(initial_investment, growth_rate, growth_periods):
    
    val = initial_investment * (1+growth_rate)**(growth_periods*growth_rate)
    
    return val
    
    