largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        number = int(num)
    except:
        print "Invalid input"
        continue
    
    if largest is None or smallest is None:
        largest=smallest=number
    else:
        if number> largest:
        	largest=number
        if number<smallest:
            smallest=number
print "Maximum is "+ str(largest)
print "Minimum is "+ str(smallest)