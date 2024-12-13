import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def create_code_table(node, prefix="", code_table={}):
    if node is not None:
        if node.char is not None:
            code_table[node.char] = prefix
        create_code_table(node.left, prefix + "0", code_table)
        create_code_table(node.right, prefix + "1", code_table)
    return code_table

def encode_text(text, code_table):
    return ''.join(code_table[char] for char in text)

def decode_text(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return ''.join(decoded_text)

def huffman_coding(text):
    if not text:
        return "", None, {}

    root = build_huffman_tree(text)
    code_table = create_code_table(root)
    encoded_text = encode_text(text, code_table)
    return encoded_text, root, code_table

def main():
    text = input("Introduce el mensaje de texto: ")
    encoded_text, root, code_table = huffman_coding(text)

    if root is None:
        print("El mensaje está vacío.")
        return

    decoded_text = decode_text(encoded_text, root)

    print(f"Mensaje original: {text}")
    print(f"Mensaje codificado: {encoded_text}")
    print(f"Mensaje decodificado: {decoded_text}")
    print(f"Número de bits en el mensaje codificado: {len(encoded_text)}")
    print(f"Número de caracteres en el mensaje original: {len(text)}")

    if len(text) <= 10:  # Mostrar el árbol de Huffman si el mensaje es corto
        print("\nÁrbol de Huffman:")
        print_huffman_tree(root)

def print_huffman_tree(node, indent=""):
    if node is not None:
        print_huffman_tree(node.right, indent + "   ")
        print(f"{indent}{node.char if node.char else '*'}")
        print_huffman_tree(node.left, indent + "   ")

if __name__ == "__main__":
    main()