latin_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
              '123456789!?&#~={}[]()+-*,.;:_°|@§`%£$¤¨µ^<>²'

def get_string_from_code(coded_list, key):
    """
    @lenth : Nombre de caracteres
    @key : string comportant tous les caracteres utilises
    """
    decoded = ''
    for char in coded_list:
        decoded += key[char]
    return decoded

def generate_password(length, key=latin_key):
    """
    @lenth : Nombre de caracteres
    @key : string comportant tous les caracteres utilises
    """

    # Initialisation
    password = []
    max_index = len(key) - 1
    coded_list = [0] * length
    split = '\n'
    running = True

    # Creation du mdp
    while running:
        index = 0
        while True:
            if coded_list[index] + 1 <= max_index:
                coded_list[index] += 1
                break
            else:
                index += 1
        password.append(get_string_from_code(coded_list, key))

    str = ''
    for char in actual_list:
        str += key[char]

    # Retour de CODE

    aa 00
    bb 11
    ab 01
    ba 10
    number > len(key)
    [0][0][0][1][0]
    [0][0][0][1][1]
    [0][0][1][1][0]



#-------------[EXECUTION CODE]-----------------------------
generated = generate_password(4, "azer")
print(generated)
