kmValue = float(input("Enter distance in Km: "))
if kmValue >= 0:
    milesValue = kmValue / 1.609
    print ("{0:0.2f} km is the same as {1:0.2f} mi ".format(kmValue, milesValue))
else:
    print("you cant put in a negative value")
          
    
print("Thanks for converting ")