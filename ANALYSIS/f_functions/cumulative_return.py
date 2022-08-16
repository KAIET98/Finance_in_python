

def cum_return(investment, return_per, periods):
    
    val = investment*(1 + return_per)**(periods)
    
    return val