import os, sys

files = os.listdir()

for file in files:
    if '.pyc' in file:
        print(file)