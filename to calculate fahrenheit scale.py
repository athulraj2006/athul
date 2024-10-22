temp=int(input("Enter temperature"))
candf=input("Is this in (C)elsius or (F)ahrenheit?")
if candf=="C" or candf=="c":
    celsius = float(temp)
    fahrenheit = (9/5*celsius) + 32
    print(temp ," Celsius is ",fahrenheit, "Fahrenheit.")
elif candf=="F" or candf=="f":
      fahrenheit = float(temp)
      celsius = (5/9*fahrenheit)-32
      print(temp," Fahrenheit is ",celsius," Celsius.")
else:
       print("Only enter C or F")