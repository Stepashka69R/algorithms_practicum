import heapq
from collections import defaultdict


class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def get_freq(string):
    freq = defaultdict(int)
    for char in string:
        freq[char] += 1
    return freq


def build_huffman_tree(freq):
    heap = []
    for char, char_freq in freq.items():
        heapq.heappush(heap, Node(char=char, freq=char_freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        combined_freq = left.freq + right.freq
        combined_node = Node(freq=combined_freq, left=left, right=right)
        heapq.heappush(heap, combined_node)

    return heap[0]


def build_codes(node, current_code, codes):
    if node.char:
        codes[node.char] = current_code
        return

    build_codes(node.left, current_code + "0", codes)
    build_codes(node.right, current_code + "1", codes)


def huffman_encode(string):
    freq = get_freq(string)
    huffman_tree = build_huffman_tree(freq)
    codes = {}
    build_codes(huffman_tree, "", codes)

    total_unique_chars = len(freq)
    total_encoded_bits = sum(len(code) * freq[char] for char, code in codes.items())

    print(f"{total_unique_chars} {total_encoded_bits}")
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")

    encoded_string = ''.join(codes[char] for char in string)
    return encoded_string


string = "Errare humanum est."
encoded_string = huffman_encode(string)
print(encoded_string)
