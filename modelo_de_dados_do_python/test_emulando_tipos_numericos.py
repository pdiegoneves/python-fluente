import unittest
from emulando_tipos_numericos import Vector

class TestVetor(unittest.TestCase):
    def test_print(self):
        v = Vector(3, 4)
        self.assertEqual(str(v), 'Vector(3, 4)')

    def test_add(self):
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)
        self.assertEqual(v1 + v2, Vector(4, 5))

    def test_abs(self):
        v = Vector(3, 4)
        self.assertEqual(abs(v), 5.0)

    def test_multiply(self):
        v = Vector(3, 4)
        self.assertEqual(v * 3, Vector(9, 12))
    

if __name__ == '__main__':
    unittest.main()