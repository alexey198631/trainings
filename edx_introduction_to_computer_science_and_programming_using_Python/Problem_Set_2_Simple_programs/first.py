"""

Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the credit card company each month.

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remaining_balance(balance, annualInterestRate, monthlyPaymentRate):

    i = annualInterestRate/12.0  # monthly interest rate
    mp = monthlyPaymentRate
    rb = balance #remaining balance

    monthes = range(1,13)
    for m in monthes:
        rb = rb*(1-mp)*(1+i)
    return print('Remaining balance:', round(rb,2))

remaining_balance(balance, annualInterestRate, monthlyPaymentRate)

"""

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

"""

def fixed_monthly_payment(balance, annualInterestRate):
    i = annualInterestRate / 12.0  # monthly interest rate
    monthes = range(1, 13)
    m = 1
    x = 0
    ub = balance
    count = 0

    while ub > 0:

        ub = balance
        x += 10
        for m in monthes:
            ub = ub - x + (ub - x) * i
        count += 1

    return print('Lowest Payment:', x,count)


def fixed_monthly_payment_m(balance, annualInterestRate):
    i = annualInterestRate / 12.0  # monthly interest rate
    monthes = range(1, 13)
    m = 1
    lb = balance/12
    hb = (balance*((1+i)**12))/12
    x = (lb + hb)/2
    ub = balance

    count = 0

    while abs(ub) > 0.01:

        ub = balance
        for m in monthes:
            ub = ub - x + (ub - x) * i

        if ub < 0:
            hb = x
        elif ub > 0:
            lb = x
        x = (lb + hb)/2
        count += 1



    return print('Lowest Payment:', round(x,2),count)

fixed_monthly_payment(99999999, 0.2)
fixed_monthly_payment_m(99999999, 0.2)
