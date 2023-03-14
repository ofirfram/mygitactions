import os
import re 
import sys


# Access the value of the EXTRACTED_DATA environment variable
extracted_data = os.environ.get('EXTRACTED_DATA')

# Print the value of the extracted data
print(f"The extracted data is: {extracted_data}")
