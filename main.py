import sys


latin_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
            '123456789!?&#~={}[]()+-*,.;:_°|@§`%£$¤¨µ^<>²'

def get_string_from_code(coded_list, key):
    """
    coded_list : list comportant les indices a prendre de key
    key : string comportant tous les caracteres utilises
    """
    decoded = ''
    for coded_char in coded_list:
        decoded += key[coded_char]
    return decoded

def write_password(str_length='1', str_per_line='1', filename='password.txt',
                   key=latin_key):
    """
    length : Nombre de caracteres
    key : string comportant tous les caracteres utilises
    """

    per_line = int(str_per_line)
    length = int(str_length)
    password = []
    pos = 0
    max_char_code = len(key) - 1
    coded_list = [0] * length
    actual_line_length = 0
    number_of_password = 0

    with open(filename, 'w') as file:
        while True:
            file.write(get_string_from_code(coded_list, key) + ' ')
            number_of_password += 1
            actual_line_length += 1
            if actual_line_length == per_line:
                file.write('\n')
                actual_line_length = 0
            if coded_list[pos] + 1 <= max_char_code:
                coded_list[pos] += 1
            else:
                pos += 1
                while pos < length and coded_list[pos] == max_char_code:
                    pos += 1
                if pos < length:
                    for i in range(pos):
                        coded_list[i] = 0
                    coded_list[pos] += 1
                    pos = 0
                else:
                    break
    print('%d passwords were written to the file: %s' % (number_of_password, filename))

write_password(*sys.argv[1:])
