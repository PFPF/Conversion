name = raw_input ("Your name:")
cm = raw_input ("How tall in cm are you:")
inch = int(int(cm) / 2.54 + 0.5)
feet = int(inch / 12)
if (inch < 0): inch = -13 ; feet = -1
inch -= 12 * feet
print ("Nice to meet you " + name + ", you are"),
if (feet > 1): print (str(feet) + " feet"),
if (feet == 1): print ("1 foot"),
if (feet > 0 and inch > 0): print("and"),
if (inch > 1): print(str(inch) + " inches tall.")
if (inch == 1): print("1 inch tall.")
if (inch == 0 and feet > 0): print ("tall.")
if ( (feet == 0 and inch == 0) or (feet < 0 or inch < 0) ): print("kidding me!")