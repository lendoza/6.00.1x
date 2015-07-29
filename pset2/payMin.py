# Problem Set 2 : Part 1

def payMin():

    '''Computes the total amount paid on credit card debt when only paying the minimum'''
      
    monthlyInterestRate = annualInterestRate / 12.0
    minMonthly = round(monthlyPaymentRate * balance,2)
    month = 0
    total = 0
    global balance
    
    while month < 12 and balance > 0:
        minMonthly = round(monthlyPaymentRate * balance,2)
        balance = balance - minMonthly
        balance = round(balance + (monthlyInterestRate * balance),2)
        month += 1
        total += minMonthly
        print 'Month: ' + str(month)
        print 'Minimum monthly payment: ' + str(minMonthly)
        print 'Remaining balance: ' + str(balance) 
    
    print 'Total paid: ' + str(total)
    print 'Remaining balance: ' + str(balance)
        
payMin()