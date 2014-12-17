penny = int(raw_input ("Enter an amount of money in cents: "))
# non-integers are not allowed

if (penny <= 0): 
	print("Kidding?")
	# integers <=0 are not allowed
	
else: 
	print(str(penny) + " cents is"),
	
	# generate nickel
	nickel = int(penny) / 5
	penny %= 5
	
	# generate quarter
	quarter = nickel / 5
	nickel %= 5
	
	# generate dime
	dime = nickel / 2
	nickel %= 2
	
	# position of "and" 
	if (penny != 0 and quarter + dime + nickel != 0): andk = 0
	elif (nickel != 0 and quarter + dime != 0): andk = 1
	elif (dime != 0 and quarter != 0): andk = 2
	else: andk = 3

	# print quarter
	if (quarter > 1): print (str(quarter) + " quarters"),
	if (quarter == 1): print ("1 quarter"),
	
	# print dime
	if (andk == 2): print("and"),
	if (dime > 1): print(str(dime) + " dimes"),
	if (dime == 1): print("1 dime"),
	
	# print nickel
	if (andk == 1): print("and"),
	if (nickel > 1): print(str(nickel) + " nickels"),
	if (nickel == 1): print("1 nickel"),
	
	# print penny
	if (andk == 0): print("and"),
	if (penny > 1): print(str(penny) + " pennies")
	if (penny == 1): print("1 penny")