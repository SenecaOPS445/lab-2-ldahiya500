#!/usr/bin/env python3
#Author: Lakshay
# Author ID: lakshay2@myseneca.ca
# Date Created: 2024/05/28
import sys

if len(sys.argv) != 3:
  print("Usage:", sys.argv[0] + " name age")
  sys.exit()
  
name = sys.argv[1]
age = sys.argv[2]

print("Hi " + name + ", you are " + str(age) + " years old.")
