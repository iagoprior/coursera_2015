def computepay(h, r):
    if h > 40:
      reg = h*r
      otp = (h-40)*(r*0.5)
      xp = reg+otp
      return xp
    else:
      xp = h*r
      return xp

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)
print("Pay", p)