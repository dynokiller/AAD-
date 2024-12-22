import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build Huffman Tree
def huffman_tree(char_freqs):
    heap = [Node(char, freq) for char, freq in char_freqs.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

# Function to generate Huffman Codes from the tree
def huffman_codes(root):
    codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    
    generate_codes(root)
    return codes

# Encoding function
def encode(text, codes):
    return ''.join([codes[char] for char in text])

# Decoding function with reversed input
def decode(encoded_text, root):
    encoded_text = encoded_text[::-1]  # Reverse the input
    current = root
    decoded_text = ""
    
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.left is None and current.right is None:  # Leaf node
            decoded_text += current.char
            current = root
            
    return decoded_text[::-1]  # Reverse the final decoded text
