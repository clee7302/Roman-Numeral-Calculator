while True:
    try:
	    x = input("Enter a whole number from 1 - 9 (without spaces): ")
	    inttX = int(x)
	    if (inttX) == 0 or 0 > (inttX):
	        print("The smallest number you enter has to be 1 ")
	    elif (inttX) > 9:
	        print("The greatest number you enter has to be 9 ")
	    else:
	        if len(x) == 1:
		        if inttX == 1:
		            first = "I"
		        elif inttX == 2:
		            first = "II"
		        elif inntX == 3:
		            first = "III"
		        elif inttX == 4:
		            first = "IV"
		        elif inttX == 5:
		            first = "V"
		        elif inttX == 6:
		            first = "VI"
		        elif inttX == 7:
		            first = "VII"
		        elif inttX == 8:
		            first = "VIII"
		        elif inttX == 9:
		            first = "IX"
		        print(first)

    except ValueError:
	    print("That was not a positive integer, you should retry ")

    while True:
	     answer = str(input('Run again? (y/n); '))
	     if answer in ('y' , 'n'):
	         break
	     print ("invalid input.")
    if answer == 'y':  
	     restart = lab(x)
    else:
	     print("Goodbye")
	     break
		
