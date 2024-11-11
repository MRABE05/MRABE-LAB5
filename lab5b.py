#!/usr/bin/env python3
# Author ID: mrabe

def append_file_string(file_name, string_of_lines):
    # Appends the provided string to the end of the specified file
    with open(file_name, 'a') as file:
        file.write(string_of_lines)


def write_file_list(file_name, list_of_lines):
    # Writes each item from the list as a separate line in the specified file
    with open(file_name, 'w') as file:
        for line in list_of_lines:
            file.write(line + '\n')


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads from the first file, writes to the second with line numbers prefixed to each line
    with open(file_name_read, 'r') as read_file, open(file_name_write, 'w') as write_file:
        for index, line in enumerate(read_file, start=1):
            write_file.write(f"{index}:{line}")


def read_file_string(file_name):
    # Reads and returns the entire content of the file as a string
    with open(file_name, 'r') as file:
        return file.read()
    
def read_file_list(file_name):
    # Reads the file and returns a list of lines without newline characters
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    # Append string to file1 and print its contents
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    # Write list to file2 and print its contents
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    # Copy file2 to file3 with line numbers and print its contents
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
