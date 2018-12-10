sMax = -1000
while True:
    summing = 0
    num = input("Give me a number: ")
    try:
        num = int(num)

    except ValueError:
        print("You have not entered a proper number.")
        break

    summing = summing + num

    if summing > sMax:
        sMax = summing

    print("The Biggest Sum is: ", sMax)