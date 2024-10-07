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