batteryLevel = float(input("Enter the phone's battery level: "))
if batteryLevel >= .2:
    print("Fill battery with white")
if batteryLevel <= .1:
    print("Fill battery with red")