#!/usr/bin/env python3
# Author ID: mrabe

import lab5b
file1 = 'seneca1.txt'
file2 = 'seneca2.txt'
file3 = 'seneca3.txt'
string1 = 'First Line\nSecond Line\nThird Line\n'
list1 = ['Line 1', 'Line 2', 'Line 3']

lab5b.append_file_string(file1, string1)

lab5b.read_file_string(file1)
# Will print 'First Line\nSecond Line\nThird Line\nFirst Line\nSecond Line\nThird Line\n'

lab5b.write_file_list(file2, list1)

lab5b.read_file_string(file2)
# Will print 'Line 1\nLine 2\nLine 3\n'

lab5b.copy_file_add_line_numbers(file2, file3)

lab5b.read_file_string(file3)
# Will print '1:Line 1\n2:Line 2\n3:Line 3\n'