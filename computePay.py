strHours = raw_input('Enter Hours:')
try:
	hours = float(strHours)
except:
	print "Error, please enter numeric input"
	quit()
strRate = raw_input('Enter Rate:')
try:
	rate = float(strRate)
except:
	print "Error, please enter numeric input"
	quit()

if hours < 40:
	pay = hours * rate
else:
	pay = 40 * rate + (hours - 40) * 1.5 * rate
print "Pay:", pay
