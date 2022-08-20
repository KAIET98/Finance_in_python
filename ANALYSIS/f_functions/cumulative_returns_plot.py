import matplotlib.pyplot as plt

def cumulative_returns_plot(data, cols): 
    """
    cols: A list of column names to plot 
    """
    
    CumulativeReturns = ((1+data[cols]).cumprod()-1) 
    CumulativeReturns.plot() 
    plt.show()