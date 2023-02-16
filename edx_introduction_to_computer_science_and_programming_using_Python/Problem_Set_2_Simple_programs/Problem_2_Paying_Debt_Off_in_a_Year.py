"""
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

- balance - the outstanding balance on the credit card
- annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,
for example:

- owest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month
(after the payment for that month is made). The monthly payment must be a multiple of $10 and is the
same for all months. Notice that it is possible for the balance to become negative using this payment scheme,
which is okay. A summary of the required math is found below:

- Monthly interest rate = (Annual interest rate) / 12.0
- Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
- Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""


def fixed_monthly_payment(balance, annualInterestRate):
    i = annualInterestRate / 12.0  # monthly interest rate
    monthes = range(1, 13)
    m = 1
    payment = 0
    count = 0
    ubalance = balance

    while ubalance > 0:
        ubalance = balance
        payment += 10
        for m in monthes:
            ubalance = ubalance - payment + (ubalance - payment) * i
        count += 1

    return print(f'Lowest Payment: {payment}')


fixed_monthly_payment(3329, 0.2)
fixed_monthly_payment(4773, 0.2)
fixed_monthly_payment(3926, 0.2)
fixed_monthly_payment(99999999, 0.2)