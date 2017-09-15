# P * R * T / 100

p = float(input("Enter the Principal amount: "))
r = float(input("Enter the Rate : "))
t = float(input("Enter the Time : "))

si = (p*r*t)/100

print('Simple intest for principal amount {0} for {1} years at the rate of {2} pa is {3} ' .format(p,t,r,si))
