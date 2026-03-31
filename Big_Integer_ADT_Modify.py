class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None

class BigIntegerList:

    def __init__(self, number):
        self.value = int(number)

    def display(self):
        print(self.value)

    def __iadd__(self, other):
        self.value += other.value
        return self
    
    def __isub__(self, other):
        self.value -= other.value
        return self
    
    def __imul__(self, other):
        self.value *= other.value
        return self
    
    def __ifloordiv__(self, other):
        self.value //= other.value
        return self
    
    def __imod__(self, other):
        self.value %= other.value
        return self
    
    def __ipow__(self, other):
        self.value **= other.value
        return self
    
    def __ilshift__(self, other):
        self.value <<= other.value
        return self
    
    def __irshift__(self, other):
        self.value >>= other.value
        return self
    
    def __ior__(self, other):
        self.value |= other.value
        return self
    
    def __iand__(self, other):
        self.value &= other.value
        return self
    
    def __ixor__(self, other):
        self.value ^= other.value
        return self
    
a = BigIntegerList("20")
b = BigIntegerList("5")

a += b
print("+= :", a.value)

a -= b
print("-= :", a.value)

a *= b
print("*= :", a.value)

a //= b
print("//= :", a.value)

a %= b
print("%= :", a.value)

a **= b
print("**= :", a.value)

a <<= b
print("<<= :", a.value)

a >>= b
print(">>= :", a.value)

a |= b
print("|= :", a.value)

a ^= b
print("^= :", a.value)