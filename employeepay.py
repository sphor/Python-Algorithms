"""
Description: Takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.

Pseudocode

     1. Significant constants
          none
     2. The inputs are
          wage
          regular hours
          overtime hours
     3. Computations:
          weeekly regular pay
          weekly overtime pay
          total weekly pay
     4. The outputs are
          total weekly pay

"""
wage = float(input("Enter the wage: "))
regularHours = int(input("Enter the regular hours: "))
overtimeHours = int(input("Enter the overtime hours: "))

regularPay = wage * regularHours
overtimePay = overtimeHours * 1.5 * wage
totalWeeklyPay = regularPay + overtimePay

print("The total weekly pay is ", "$", totalWeeklyPay)
