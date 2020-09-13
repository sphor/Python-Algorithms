"""
Description: Calculates and displays the value of a light-year.

Pseudocode

     1. Significant constants
          seconds in a year
          rate
     2. The inputs are
          none
     3. Computations:
          value = seconds in a year * rate
     4. The outputs are
          Value of meters light travels in 1 year

"""
secondsInAYear = 365*24*60**2
rate = 3*10**8
value = secondsInAYear * rate

print('Light travels ', value, ' meters in a year')
