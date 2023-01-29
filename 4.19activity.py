#Compute total bill for given party size

#input: the bill, in any currency, before surcharges
bill = 10

#input: people in the party, a positive interger
people = 4

#input: the service charge, a percentage
charge = 0.1

#output: the total bill, in the same currency
#if people < 6:
    #total = bill + bill * charge

#else:
    #total = bill

if people < 6:
    total = bill
    
else:
    total = bill + bill * charge
    
print('The total bill is', total)
