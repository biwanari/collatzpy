
import matplotlib.pyplot as plt
import numpy as np

def generateCollatzSeries(number):
    list = []
    while number!= 1:
        if number%2==0:
            number = number//2
            list.append(number)
        else:
            number = 3*number+1
            list.append(number)
    return list

def seriesAnalysis(number, collatzseries):
    even = [ x for x in collatzseries ]
    odd  = [ x for x in collatzseries if x%2==1 ]

    return f"""
    number : {number},
       - collat'z series{collatzseries}, length -> {len(collatzseries)}
       
       - even number in series 
             {even}, length -> {len(even)}
       
       - odd  numbers in series 
             {odd}, length -> {len(even)}
       """

def generateSeriesOfCollatzSuccession(number, collatzSeries):
    
    generatinglist = []
    i = 1
    while i < number:
        generatinglist.append( generateCollatzSeries(i) )
        i += 1
    return generatingList    

def printPlotOfCollatzSerie(number, collatzseries):
    x = [ i for i in collatzseries if i%2==0 ]
    y  = [ j for j in collatzseries if j%2==1 ]
    #p = plt.bar( np.array(x), np.array(y),width=0.8, color='green','orange' )
    p = plt.plot(np.array(x), np.array(y))
    p.title('even and odd number in colletz series')
    p.xlim(len(x)-1)
    p.ylin(len(y)-1)
    p.xlabel(even)
    p.ylabel(odd)
    return p.show()

if __name__ == "__main__":
    pass