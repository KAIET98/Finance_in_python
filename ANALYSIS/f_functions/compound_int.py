

def compound_int(initial_investment, growth_rate, growth_periods, compound_periods_1):
    
    invest = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
    
    return invest