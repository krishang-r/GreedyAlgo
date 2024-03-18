global code 
code = []

def huffman_coding(character, frequency):

    length = len(character)

    freq_char_list = []

    for i in range(length):
        freq_char_list.append([frequency[i], character[i]])

    freq_char_list.sort()

    while len(freq_char_list) > 1:
        node = [freq_char_list[0], freq_char_list[1]]
        net_freq = freq_char_list[0][0] + freq_char_list[1][0]
        freq_char_list.pop(0)
        freq_char_list.pop(0)
        freq_char_list.append([net_freq, node])
        freq_char_list.sort()

    huffman_tree = freq_char_list[0]
    generate_huffman_codes(huffman_tree, "")

def generate_huffman_codes(node, current_code):
    global code
    if isinstance(node[1], list):  # Internal node
        generate_huffman_codes(node[1][0], current_code + '0')
        generate_huffman_codes(node[1][1], current_code + '1')
    else:  # Leaf node
        print(node[1], ":", current_code)
        code.append([node[1], current_code])

character = ['a', 'b', 'c', 'd', 'e', 'f']
frequency = [5, 9, 12, 13, 16, 45]
huffman_coding(character, frequency)

print(code)