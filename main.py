# this function calculates the future value
def future_value(p, i, t):
    # calculate the future value of the account after the specified time period
    f = p*(1+i)**t
    # show the result
    print("After ", t, " months, you will have $", format(f, '.2f'), " in your account.", sep="")


# the present value of the account
p = float(input('Enter the account’s present value: '))
# the monthly interest rate
i = float(input("Enter the monthly interest rate: "))
# the number of months
t = int(input("Enter the number of months that the money will be left in the account: "))
# call the future_value function
future_value(p, i, t)