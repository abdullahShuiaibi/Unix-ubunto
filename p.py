#!/user/bin/python

import subprocess

print("Starting Python Program")

output= subprocess.check_output(["ls","-al","/home/abdullah"])

for line in output.splitlines():
    print(line)

if (10>9):
    print("The laws of the universe is good")
else:
    print("NOOOOOOOOOOOOOO")

print("Leaving goodbye")
