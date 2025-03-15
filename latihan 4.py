class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        raise TypeError("Operand harus berupa objek Vector")

    def __mul__(self, skalar):
        if isinstance(skalar, (int, float)):
            return Vektor(self.x * skalar, self.y * skalar)
        raise TypeError("Operand harus berupa angka (int atau float)")

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

v1 = Vektor(2, 3)
v2 = Vektor(4, 5)

# Menjumlahkan dua vektor
v3 = v1 + v2
print(f"\nV1 ({v1})  + V2 ({v2}) \n= {v3}")  

# Mengalikan vektor dengan skalar
v4 = v1 * 3
print(f"\nv1 ({v1}) * 3 \n= {v4}") 