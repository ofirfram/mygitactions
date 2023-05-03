import os
import re 
import sys


# # Access the value of the EXTRACTED_DATA environment variable
# extracted_data = os.environ.get('EXTRACTED_DATA')
# print(extracted_data)

# pattern = r"SKIP_TESTS=.*?(?=[A-Z_]+=|$)"
# match = re.search(pattern, extracted_data)
# if match:
#     desired_str = match.group(0)
#     print(desired_str)
# else:
#     print("Desired string not found.")

os.popen("git clone https://github.com/ofirfram/test.git").read()
filename = "test/testit.conf"
print(filename)
file_read = open(filename, "r")
test_to_print = file_read.read()
file_read.close()
print(test_to_print)
