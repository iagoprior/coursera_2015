#  Write a program to prompt the user for hours and rate per hour
#  using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour
#  to test the program (the pay should be 96.25).

hrs = input("Enter Hours:")
rate = input("Enter rate:")
usf = float(hrs)*float(rate)
st = str(usf)
print('Pay: ' + st)