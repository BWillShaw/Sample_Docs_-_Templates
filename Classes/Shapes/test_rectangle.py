
import unittest
from rectangle import rectangle  

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.rect = rectangle(4, 5)
    
    def test_calc_area(self):
        self.assertEqual(self.rect.calc_area(), 20)
    
    def test_calc_perimeter(self):
        self.assertEqual(self.rect.calc_perimeter(), 22)
    
    def test_str_method(self):
        self.rect.calc_area()
        self.rect.calc_perimeter()
        self.assertEqual(str(self.rect), "The rectangle has a length of 4 and a width of 5. " \
                                         "The perimeter is 22 and the area is 20.")
    
if __name__ == "__main__":
    unittest.main()

