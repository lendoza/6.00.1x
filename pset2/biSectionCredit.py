# Problem Set 2 : Part 3

'''Utilizes Bi-section Search to find the lowest monthly payment needed to pay a credit card off in 12 months'''

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
epsilon = 0.01 


while abs(balance) > epsilon:
    balance = originalBalance
    # Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound) / 2 + lowerBound

    # Test if this payment value is sufficient to pay off the entire balance in 12 months
    for month in range(12):
        balance -= payment
        balance *= 1 + monthlyInterestRate

    # Reset bounds based on the final value of balance
    if balance > 0:
        # If the balance is too big, need higher payment so we increase the lower bound
        lowerBound = payment
    else:
        # If the balance is too small, we need a lower payment, so we decrease the upper bound
        upperBound = payment


print "Lowest Payment:", round(payment, 2)