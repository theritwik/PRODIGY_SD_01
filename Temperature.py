#Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

# Define a function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
  return celsius + 273.15

# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

# Define a function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
  return (fahrenheit - 32) * 5/9 + 273.15

# Define a function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
  return kelvin - 273.15

# Define a function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
  return (kelvin - 273.15) * 9/5 + 32

# Main program
print("Temperature Conversion Program")
print("----------------------------")

# Prompt user for input
temperature = float(input("Enter a temperature value: "))
unit = input("Enter the original unit of measurement (C, F, or K): ")

# Convert temperature based on original unit
if unit.upper() == "C":
  fahrenheit = celsius_to_fahrenheit(temperature)
  kelvin = celsius_to_kelvin(temperature)
  print(f"{temperature} degrees Celsius is equal to:")
  print(f"{fahrenheit:.2f} degrees Fahrenheit")
  print(f"{kelvin:.2f} Kelvin")
elif unit.upper() == "F":
  celsius = fahrenheit_to_celsius(temperature)
  kelvin = fahrenheit_to_kelvin(temperature)
  print(f"{temperature} degrees Fahrenheit is equal to:")
  print(f"{celsius:.2f} degrees Celsius")
  print(f"{kelvin:.2f} Kelvin")
elif unit.upper() == "K":
  celsius = kelvin_to_celsius(temperature)
  fahrenheit = kelvin_to_fahrenheit(temperature)
  print(f"{temperature} Kelvin is equal to:")
  print(f"{celsius:.2f} degrees Celsius")
  print(f"{fahrenheit:.2f} degrees Fahrenheit")
else:
  print("Invalid unit. Please enter C, F, or K.")
