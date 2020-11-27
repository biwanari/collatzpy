

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
    even = [ x for x in collatzseries if x%2==0 ]
    odd  = [ x for x in collatzseries if x%2==1 ]

    return f"""
    number : {number} 
       - collat'z series{collatzseries}, {len(collatzseries)}
       
       - even number in series 
             {even}, length {len(even)}
       
       - odd  numbers in series 
             {odd}, length {len(even)}
       """


if __name__ == "__main__":
    number = int(input("digit number \n"))
    x = generateCollatzSeries(number)
    print(seriesAnalysis(number, x))