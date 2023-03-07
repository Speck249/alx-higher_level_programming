#!/usr/bin/python3

def uppercase(str):
 for i in range(len(str)):
  if ord(str[i]) > 96 and ord(str[i]) < 123:
   j = 32
  else:
   j = 0
  
  print("{:c}".format(ord(str[i]) - j), end="")
 print()
