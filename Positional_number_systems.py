# Write a Python script that converts a string into its ASCII and Unicode code points.
# For ASCII characters, display their integer values. For Unicode characters outside of
# the ASCII range (e.g., Chinese, Arabic), display their Unicode code points.

string = "Hello, ζηθ!"
for el in string:
  nr = ord(el)
  if nr <= 128:
    print(f"charcter: {el}, ASCII Code: {nr}")
  elif nr > 128:
    print(f"character: {el}, Unicode Code Point: {ord(el):04X}")



#From a decimal number to a hexadecimal number
def decimal_to_hexadecimal(decimal_number):
  hexadecimal_digits = '0123456789ABCDEF'
  hexadecimal_number = ""

  while decimal_number > 0:
    remainder = decimal_number % 16
    hexadecimal_number = hexadecimal_digits[remainder] + hexadecimal_number
    decimal_number //= 16

  return hexadecimal_number

decimal_number = int(input("Enter a decimal number: "))
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print("The hexadecimal represntation of", decimal_number, "is", hexadecimal_number)


# From a hexadecimal number to a decimal number

def hexadecimal_to_decimal(hexadecimal_number):
  hex_ints = []
  hex_dict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}


  hexadecimal_elements = [el for el in hexadecimal_number]

  for el in hexadecimal_elements:
    try:
      hex_ints.append(int(el))
    except ValueError:
      hex_ints.append(hex_dict[el])

  power = 0
  order = 0
  hex_values = []
  hex_ints = hex_ints[::-1]

  while order < len(hex_ints):
    hex_values.append(hex_ints[order] * (16 ** power))
    order += 1
    power += 1

  return sum(hex_values)

hexadecimal_number = str(input("Enter a hexadecimal number:  "))
decimal_number = hexadecimal_to_decimal(hexadecimal_number)
print(f"The decimal representation of {hexadecimal_number} is {decimal_number}")


# From a decimal number to a binary
def decimal_to_binary(decimal_number):
  binary_representation = ''

  while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number //= 2

  return binary_representation

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print("The binary represntation of", decimal_number, "is", binary_number)

# From a binary number to a decimal number
def binary_to_decimal(binary_number):
    order = 0
    power = 0
    decimal_number = []

    binary_number = [int(el) for el in binary_number][::-1]

    while order < len(binary_number):
        decimal_number.append(binary_number[order] * (2 ** power))
        order += 1
        power += 1

    return sum(decimal_number)

binary_number = str(input("Enter a binary number: "))
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal representation of {binary_number} is {decimal_number}")