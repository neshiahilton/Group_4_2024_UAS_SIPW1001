class Basic:
    def euclids_algorithm(self, a, b):
        """
        Euclid's Algorithm to calculate GCD (Greatest Common Divisor)
        :param a: First number
        :param b: Second number
        :return: GCD of a and b
        """
        while b != 0:
            a, b = b, a % b
        return a

    def huffman_coding(self, data):
        """
        Huffman Coding to find character frequencies (simple example)
        :param data: Input string
        :return: Frequency dictionary
        """
        from collections import Counter
        frequency = Counter(data)
        return sorted(frequency.items(), key=lambda x: x[1])

    def union_find(self, n):
        """
        Simple Union-Find implementation
        :param n: Number of elements
        :return: Parent array after union-find operations
        """
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        return parent


 # Testing
if __name__ == "__main__":
    basic = Basic()
    
    # Testing Euclid's Algorithm
    print("GCD of 48 and 18 is:", basic.euclids_algorithm(48, 18))
    print("GCD of 101 and 103 is:", basic.euclids_algorithm(101, 103))

    # Testing Huffman Coding
    text = "huffman coding example"
    print("Character frequencies (Huffman):", basic.huffman_coding(text))

    # Testing Union-Find
    n = 5  # Elements: 0 to 4
    parent = [i for i in range(n)]
    print("Initial parent array:", parent)
    print("Union-Find result after union:", basic.union_find(n))
