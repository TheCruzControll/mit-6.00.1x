r = annualInterestRate/12
lowerBound = balance/12
upperBound = (balance*((1+r)**12))/12
monthlyPaymentRate = (lowerBound+upperBound)/2
init_balance = balance
monthlyInterestRate = annualInterestRate/12
epsilon = 0.01
while abs(balance)>epsilon:
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        lowerBound = monthlyPaymentRate
    elif balance <= 0:
        upperBound = monthlyPaymentRate
    monthlyPaymentRate = (lowerBound+upperBound)/2
print('Lowest Payment:', str(round(monthlyPaymentRate,2)))