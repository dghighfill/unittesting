from calculator import Calculator

cal: Calculator = Calculator()

print(f"The Calculator Power is on:{cal.is_on()}")
cal.power_on()
print(f"The Calculator Power is on: {cal.is_on()}")
cal.power_off()
print(f"The Calculator Power is on: {cal.is_on()}")