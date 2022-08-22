

def kurtosis_valoration(kurtosis):
    
    if float(kurtosis) < 3: 
        
        print('EL rendimiento está mas concentrado en la media que en las colas')
        
    else: 
        
        print('El rendimiento está mas concentrado en las colas')