
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
    
    odd  = [ i for i in collatzseries if i%2==1 ]
    even = [ i for i in collatzseries if i%2==0 ]

    return f"""
    number : {number},
       - collat'z series{collatzseries}, length -> {len(collatzseries)}

       - even number in series 
             {even}, length -> {len(even)}
       
       - odd  numbers in series 
             {odd}, length -> {len(even)}
       """

def generateMoreSeries(number):
    for i in range(2, 21):
        print(seriesAnalysis(i, generateCollatzSeries(i)))
        print("  ")

if __name__ == "__main__":
    pass