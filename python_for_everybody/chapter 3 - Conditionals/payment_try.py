hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter a numeric input")
    quit()

if h > 40:
    reg = h*r
    otp = (h-40)*(r*0.5)
    xp = reg+otp
else:
    xp = h*r

print(xp)