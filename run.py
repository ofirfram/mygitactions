import os
import re 
import sys


# Access the value of the EXTRACTED_DATA environment variable
extracted_data = os.environ.get('EXTRACTED_DATA')
print(extracted_data)

extracted_data = extracted_data.split()
print(extracted_data)
print("ff")

print("@@@@@@@@@") 

for line in extracted_data:
  print(line + "\n")
  if re.search("^SKIP_TESTS", line):
      print("QPM_GUI " + line)
