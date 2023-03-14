import os

contents = os.getenv('contents')

print(contents)

contents = contents.split()
print(contents)
for line in contents:
    if re.search("^SKIP_TESTS", line):
         print("QPM_GUI " + line)
