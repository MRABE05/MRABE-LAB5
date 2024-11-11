#!/usr/bin/env python3
# Author ID: mrabe

def add(number1, number2):
    try:
        # Try to convert inputs to floats and add them
        result = float(number1) + float(number2)
        return result
    except (ValueError, TypeError):
        # If there's an error (like a non-numeric input), return the specified error message
        return 'error: could not add numbers'

def read_file(filename):
    try:
        # Open the file and read all lines into a list
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError):
        # If there's an error (like file not found), return the specified error message
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                   # works
    print(add('10', 5))                 # works
    print(add('abc', 5))                # exception
    print(read_file('seneca2.txt'))     # works
    print(read_file('file10000.txt'))   # exception
