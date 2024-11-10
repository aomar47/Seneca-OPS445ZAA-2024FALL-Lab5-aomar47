#!/usr/bin/env python3
# Author ID: aomar47


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # returns its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return [line.strip() for line in lines]

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    f = open(file_name_read, 'r')
    list_of_lines = f.readlines()
    f.close()

    f = open(file_name_write, 'w')
    number_for_line = 1
    for item in list_of_lines:
        formatted_line = str(number_for_line) + ':' + item.strip()
        f.write(formatted_line + '\n')
        number_for_line += 1
    f.close()

if __name__ == '__main__':
    # Define file names
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    # Define string and list to be written to files
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    # Append string to file1 and print its content
    append_file_string(file1, string1)
    print(read_file_string(file1))

    # Write list to file2 and print its content
    write_file_list(file2, list1)
    print(read_file_string(file2))

    # Copy content from file2 to file3 with line numbers and print its content
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

