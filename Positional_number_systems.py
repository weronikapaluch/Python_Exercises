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

