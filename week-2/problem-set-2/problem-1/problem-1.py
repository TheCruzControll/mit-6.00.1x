r= annualInterestRate/12
payment=balance*monthlyPaymentRate
for i in range(12):
    payment=balance*monthlyPaymentRate
    unpaidBalance = balance-payment
    balance = unpaidBalance+(r*unpaidBalance)
print('Remaining balance: ' + str(round(balance, 2)))