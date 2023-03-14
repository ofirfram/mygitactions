import os
import re 

contents = os.getenv('contents')

print(contents)

print(type(contents))
contents = str(contents)
print(type(contents))

contents = contents.split()
for line in conetnts:
    if re.search("^SKIP_TESTS", line):
        print("QPM_GUI " + line)
