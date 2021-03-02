# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:52:28 2021

@author: sin
"""
def roman(n):
    '''
    Convert the given arabic number to roman numerals.
    INPUT the arabic number to convert
    RETURN roman numerals equivalent to the given arabic number
    '''
    # def str_to_list_digits(n):
    #     return [int(x) for x in str(n)]
    
    if n > 3999:
        print("3999 is the larget roman number")
        return -1
    if n < 1:
        print ("1 is the smallest roman number")
    def int_to_list_digits(number, list_length = 4):
        '''
        get a integer and split it to digits

        Parameters
        ----------
        number : integer
            DESCRIPTION.
        list_length : integer
            the size of our output list.

        Returns
        -------
        list : list
            split an integer andreturn them as a list.

        '''
        list = []
        for i in range(list_length):
            list.append(number%(10*(10**i))//(10**i))
        return list
        
    
    def digit_to_roman(list):
        units, tens, hundreds, thousands = list
        
        result = ''
        if thousands > 0 and thousands < 4: 
            if thousands == 1:
                result = 'M'
            elif thousands == 2:
                result = 'MM'
            elif thousands == 3:
                result = "MMM"
        if hundreds > 0:
            if hundreds == 1:
                result = result + 'C'
            elif hundreds == 2:
                result = result + 'CC'
            elif hundreds == 3:
                result = result + 'CCC'
            elif hundreds == 4:
                result = result + 'CD'
            elif hundreds == 5:
                result = result + 'D'
            elif hundreds == 6:
                result = result + 'DC'
            elif hundreds == 7:
                result = result + 'DCC'
            elif hundreds == 8:
                result = result + 'DCCC'
            elif hundreds == 9:
                result = result + 'CM'
        if tens > 0:
            if tens == 1:
                result = result + 'X'
            elif tens == 2:
                result = result + 'XX'
            elif tens == 3:
                result = result + 'XXX'
            elif tens == 4:
                result = result + 'XL'
            elif tens == 5:
                result = result + 'L'
            elif tens == 6:
                result = result + 'LX'
            elif tens == 7:
                result = result + 'LXX'
            elif tens == 8:
                result = result + 'LXXX'
            elif tens == 9:
                result = result + 'XC'
        if units > 0:
            if units == 1:
                result = result + 'I'
            elif units == 2:
                result = result + 'II'
            elif units == 3:
                result = result + 'III'
            elif units == 4:
                result = result + 'IV'
            elif units == 5:
                result = result + 'V'
            elif units == 6:
                result = result + 'VI'
            elif units == 7:
                result = result + 'VII'
            elif units == 8:
                result = result + 'VIII'
            elif units == 9:
                result = result + 'IX'
        return result
    
    return digit_to_roman(int_to_list_digits(n))

def arabic(n):
    '''
    Convert the given roman numerals to an arabic nuumber.
    INPUT the roman numerals to convert
    RETURN arabic number equivalent to the given roman numerals
    '''
    result = 0
    
    def value(x):  
        if x == 'I':
            t = 1
        elif x == 'V':
            t = 5
        elif x == 'X':
            t = 10
        elif x == 'L':
            t = 50
        elif x == 'C':
            t = 100
        elif x == 'D':
            t = 500
        elif x == 'M':
            t = 1000
        else:
            t = -1
        return t
   
    if len(n) == 1:
        result = value(n)
        if result == -1:
            print('invalid input')
            return -1
        else:
            #print('Invalid Roman number. \nplease inter valid number' )
            return result
    else:
        
        i = 0
        while i < len(n)-1:
            t = value(n[i])
            t_next = value(n[i+1])
            
            if t == -1 or t_next == -1:
                print("invalid input")
                return -1 
                
                #print('Invalid Roman number. \nplease inter valid numbers' )
           
            if t >= t_next:
                result = t + result
            else:
                
                result = result-(t)
            
            if i+1 == len(n)-1:
                result = result + t_next
            
            i += 1
       
        #check the input
        if n != roman(result):
            print ("{} is not a roman number".format(n) )
            return -1
        return result

# check the functions:
import pandas as pd
df = pd.read_csv("roman_arabic_numbers_list.csv", header = None , names = ['arabic', 'roman'])
print(df.columns)
arabic_column = df['arabic']
roman_column = df['roman']

#check roman()
for i in range(1, 4000):
    if roman_column[i - 1] != roman(i):
        print("roman {} is difer from roman({}: {})".format(roman_column[i - 1], i, roman(i)))
        print('false', end = ' ')
#check arabic()
for i in range(1, 4000):
    if arabic(roman(i)) != i:
        print("roman: {} and arabic is: {} and the i is: {}". format(roman(i), arabic(roman(i)), i))
for i in range(3999
               ):
    if arabic(roman_column[i]) != i+1:
        print("you function is sucks")
print (arabic('XIIIII'))
