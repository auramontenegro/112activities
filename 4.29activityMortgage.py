# Generate the monthly outstanding mortgage

# Input: annual interest rate, a floating-point percentage rate = 0.05
rate = 0.05

# Input: monthly payment, a positive integer in a currency payment = 200
payment = 200

# input/Output: mortgage, a positive number, same currency mortgage = 1000
mortgage = 1000

print('Outstanding mortgage: ', mortgage)
while not (mortgage == 0 or mortgage < 0):
    interest = mortgage * rate / 12
    mortgage =  mortgage + interest - payment
    print('Outstanding mortgage:', mortgage)
