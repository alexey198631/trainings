"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10.
Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent
amount (in other words, the monthly payment is a multiple of $0.01).
Does your code still work? It should, but you may notice that your code runs more slowly,
especially in cases with very large balances and interest rates.

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running
into the problem of slow code? We can make this program run faster using a technique introduced in lecture -
bisection search!

The following variables contain values as described below:

- balance - the outstanding balance on the credit card
- annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off
the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is
the obvious answer, but you can do better than that.
If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance,
so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly,
we paid off the entire balance at the end of the year.
What we ultimately pay must be greater than what we would've paid in monthly installments,
because the interest was compounded on the balance we didn't pay off each month.
So a good upper bound for the monthly payment would be one-twelfth of the balance,
after having its interest compounded monthly for an entire year.

In short:

- Monthly interest rate = (Annual interest rate) / 12.0
- Monthly payment lower bound = Balance / 12
- Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search
(for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment
to the cent (no more multiples of $10) such that we can pay off the debt within a year.
Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2
to compare!). Produce the same return value as you did in Problem 2.
"""


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

    return print('Lowest Payment:', round(x, 2))


fixed_monthly_payment_m(320000, 0.2)
fixed_monthly_payment_m(99999999, 0.2)