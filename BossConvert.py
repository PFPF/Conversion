# Super converter which took me 2 hours... Units are crazy.

print("\n\033[1mffff\033[1mThis is a super converter. You can convert many types of units. ")
print("For each item you need to input at first a magnitude then a unit. (items are added together)")
print("At last, enter \"end\" and, in a new line, the unit you want to convert to.\n\nExample:")
print(">5\n>ft\n>8\n>in\n>end\n>cm\n") # an example
print("Supported units: m,cm,ft,in,yd,mi; kg,g,t,lb,oz,gr; J,kWh,kCal; Pa,kPa,Bar,atm,mmHg.\n") # claim the supported units

def ordinal(n):  # a simple function that 1 -> "st", 2 -> "nd", 4 -> "th"...
	if (n % 100 >= 11 and n % 100 <= 13): return "th"  # eleventh...
	if (n % 10 == 1): return "st"
	if (n % 10 == 2): return "nd"
	if (n % 10 == 3): return "rd"
	
	return "th"  # because other situations are already excepted
	
i = 1 # Ordinal number of the coming item
itemNum = 0; itemUnit = "Unknown"; # initializing

# 0: length, 1: pressure, 2: mass, 3: work
unitType = {'m':0, 'cm':0, 'ft':0, 'in':0, 'yd':0, 'mi':0, 'pa':1, 'kpa':1, 'bar':1, 'atm':1, 'mmhg':1, 'kg':2, 'g':2, 't':2, 'lb':2, 'oz':2, 'gr':2, 'j':3, 'kwh':3, 'kcal':3}

# Each unit has its relative "value"
value = {'m':100.0, 'cm':1.0, 'ft':30.48, 'in':2.54, 'yd':91.44, 'mi':160934.4, 'kg':1000.0, 'g':1.0, 't':1000000.0, 'lb':453.59237, 'oz':28.349523125, 'gr':0.06479891, 'j':1.0, 'kwh':3600000.0, 'kcal':4185.851821, 'pa':0.00750061682, 'kpa':7.50061682, 'bar':750.061682, 'atm':760.0, 'mmhg':1.0}

groupType = -1 # at first we initialize it -1
sumValue = 0.0 # total value
sent = "(" # initializing

while True:
	
	itemNum = raw_input("\nEnter the {0}{1} magnitude:".format(i, ordinal(i))) # magnitude
	
	try:
		itemNum = float(itemNum)
	except ValueError: # if not a number
		if(itemNum.lower() != "end"): 
			print("The magnitude should be a number. Please try again.")
			continue # back
	
	itemUnit = raw_input("Enter the {0}{1} unit:".format(i, ordinal(i))).lower() # lowered unit
	
	try:
		if(groupType != -1 and unitType[itemUnit] != groupType): # different type with the previous
			print("That's not in the same type of the previous unit. Please try again.")
			continue # back
		groupType = unitType[itemUnit]
	except KeyError: # if the user entered the wrong unit...
		print("Please use the units that are supported. For example, check that did you input \"ft\" instead of \"feet\".")
		continue # back
	
	if(str(itemNum).lower() == "end"): break # if it is end then break now
	
	sumValue += itemNum * value[itemUnit] # magnitude * value per unit = value
	sent += str(itemNum) + itemUnit + " + " # eg. "3ft + "
	
	i += 1 # Ordinal increase 1

# remove the last " + "
print ("\n" + sent.rstrip(" +") + ") is " + str(sumValue / value[itemUnit]) + itemUnit + ".")