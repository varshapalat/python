def computepay(h,r):
    if h>40:
        pay = (h-40)*r*1.5 + 40*r
    else:
        pay = h*r
    return pay

str_hrs = raw_input("Enter Hours:")
str_rate = raw_input("Enter rate:")
hrs = float(str_hrs)
rate = float(str_rate)
p = computepay(hrs,rate)
print p