class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None

class BigInteger:

    def __init__(self, number):
        self.head = None

        # reverse the number so least significant digit comes first
        for digit in reversed(number):
            self.insert(int(digit))

    def insert(self, digit):
        new_node = Node(digit)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def display(self):
        digits = []
        current = self.head

        while current:
            digits.append(str(current.digit))
            current = current.next

        print("".join(reversed(digits)))

num = BigInteger("45839")

num.display()