latin_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
              '123456789!?&#~={}[]()+-*,.;:_°|@§`%£$¤¨µ^<>²'

def get_string_from_code(coded_list, key):
    """
    @coded_list : list comportant les indices a prendre de key
    @key : string comportant tous les caracteres utilises
    """
    decoded = ''
    for char in coded_list:
        decoded += key[char]
    return decoded

def generate_password(length, key=latin_key):
    """
    @length : Nombre de caracteres
    @key : string comportant tous les caracteres utilises
    """

    # Initialisation
    password = []
    pos = 0
    max_char_code = len(key) - 1
    coded_list = [0] * length
    split = '\n'

    # Creation du mdp
    while True:
        if coded_list[pos] + 1 <= max_char_code:
            coded_list[pos] += 1
            password.append(get_string_from_code(coded_list, key))
        else:
            pos += 1
            while pos < length and coded_list[pos] == max_char_code:
                pos += 1
            if pos < length:
                for i in range(pos):
                    coded_list[i] = 0
                coded_list[pos] += 1
                password.append(get_string_from_code(coded_list, key))
                pos = 0
            else:
                break
    # Retour de CODE
    return password

#-------------[EXECUTION CODE]-----------------------------
generated = generate_password(4)
print(generated)
print(len(generated))
