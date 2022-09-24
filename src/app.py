from calculator import Calculator

cal: Calculator = Calculator()

val1 = 2
val2 = 2

cal.power_on()
print(f"The value of {val1} + {val2} is {cal.add(val1,val2)}")
