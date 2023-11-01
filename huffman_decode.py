def huffman_decode(code_dict, encoded_string):
    reverse_dict = {code: char for char, code in code_dict.items()}
    decoded_string = ""
    current_code = ""
    for bit in encoded_string:
        current_code += bit
        if current_code in reverse_dict:
            decoded_string += reverse_dict[current_code]
            current_code = ""
    return decoded_string


code_dict = {
    ' ': '1011',
    '.': '1110',
    'D': '1000',
    'c': '000',
    'd': '001',
    'e': '1001',
    'i': '010',
    'm': '1100',
    'n': '1010',
    'o': '1111',
    's': '011',
    'u': '1101'
}

encoded_string = '100011110001001101000111111011001010011000010110011010111110'

decoded_string = huffman_decode(code_dict, encoded_string)
print(decoded_string)
