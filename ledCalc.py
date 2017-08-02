print("LED RESISTOR CALCULATOR")
resistor = 0
sourceV = float(input('Input supply voltage: '))
fwdV = int(input('Input forward voltage eg 2: '))
currentI = float(input('Input LED current in default [20mA] : ')or '20')

currentI = currentI / 1000

resistor = (sourceV - fwdV)/ currentI

print()
print('The resistor should be near {} ohms'.format(resistor))
