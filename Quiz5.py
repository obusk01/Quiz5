# Olivia Busk Quiz 5

def tire_pressure(pres):
    if pres < 28:
        print("Tire pressure is low")
    else:
        print("None")

tire_pressure(19)
tire_pressure(29)

def thermostat(temp):
    if temp <= 52:
        print("The heater is on")
    elif 52<temp<71:
        print("Heater and AC are off")
    else:
        print("AC is on")

thermostat(34)
thermostat(81)
thermostat(65)

def basket(fruit):
    if fruit=="banana":
        print("Banana, it is")
    elif fruit=="cherry":
        print("I cherish you")
    elif fruit=="apple":
        print("I applesolutely like you!")
    elif fruit=="orange":
        print("Orange you glad to see me?")
    elif fruit=="melon":
        print("You are one in a melon")

basket("melon")
basket("banana")
basket("cherry")
