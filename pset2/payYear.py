# Problem Set 2 : Part 2

'''Computes the lowest montly payment needed to pay off credit card debt in 12 months'''

monthlyPayment = 0
monthlyInterestRate = annualInterestRate /12
newbalance = balance
month = 0

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance

    for month in range(1,13):
        newbalance -= monthlyPayment
        newbalance += monthlyInterestRate * newbalance
        month += 1
print " Lowest Payment:", monthlyPayment