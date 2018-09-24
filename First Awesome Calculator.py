print ("It's an easy calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = int(input("Choose the type of action: 1- addition, 2- subtraction, 3- multiplication, 4-division, 5-exponentiation, 6-rooting "))
d = input("If you want to get only integers, select 1, on the contrary select 2: ")

if (c == 1):
    result = a + b
    if (d == '1'):
        print ("The result is: ", int(result))
    elif (d == '2'):
        print ("The result is: ", float(result))
elif (c == 2):
    result = a - b
    if (d == '1'):
        print ("The result is: ", int(result))
    elif (d == '2'):
        print ("The result is: ", float(result))
elif (c == 3):
    result = a * b
    if (d == '1'):
        print ("The result is: ", int(result))
    elif (d == '2'):
        print ("The result is: ", float(result))
elif (c == 4):
    if (b == 0):
        print ("Cannot be divided by 0!")
        sys.exit()
    elif (b > 0 or b < 0):
        result = a / b
        if (d == '1'):
            print ("The result is: ", int(result))
        elif (d == '2'):
            print ("The result is: ", float(result))
elif (c == 5):
    result = a ** b
    if (d == '1'):
        print ("The result is: ", int(result))
    elif (d == '2'):
        print ("The result is: ", float(result))
elif (c == 6):
    result = a % b
    if (d == '1'):
        print ("The result is: ", int(result))
    elif (d == '2'):
        print ("The result is: ", float(result))
else:
    print ("Choose the correct number")