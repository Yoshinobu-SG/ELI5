month = int(input("Enter month [1-12]: "))
if month <1 or month > 12:
    print("Error")
elif month >= 10:
    print("Fourth quarter")
elif month >= 7:
    print("Third quarter")
elif month >= 4:
    print("Second quarter")
elif month >= 1:
    print("F quarter")
