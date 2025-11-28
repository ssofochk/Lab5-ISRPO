import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_basic(self):
        res = circle_area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = circle_area(2.5)
        self.assertAlmostEqual(res, math.pi * 2.5 * 2.5)

    def test_perimeter_basic(self):
        res = circle_perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = circle_perimeter(2.5)
        self.assertAlmostEqual(res, 2 * math.pi * 2.5)


class SquareTestCase(unittest.TestCase):
    def test_area_basic(self):
        res = square_area(4)
        self.assertEqual(res, 16)

    def test_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = square_area(2.5)
        self.assertEqual(res, 6.25)

    def test_perimeter_basic(self):
        res = square_perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = square_perimeter(2.5)
        self.assertEqual(res, 10)


class RectangleTestCase(unittest.TestCase):
    def test_area_basic(self):
        res = rectangle_area(3, 7)
        self.assertEqual(res, 21)

    def test_area_zero(self):
        res = rectangle_area(0, 5)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = rectangle_area(2.5, 4)
        self.assertEqual(res, 10)

    def test_perimeter_basic(self):
        res = rectangle_perimeter(3, 7)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = rectangle_perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_perimeter_float(self):
        res = rectangle_perimeter(2.5, 4)
        self.assertEqual(res, 13)


class TriangleTestCase(unittest.TestCase):
    def test_area_basic(self):
        res = triangle_area(10, 6)
        self.assertEqual(res, 30)

    def test_area_zero(self):
        res = triangle_area(0, 6)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = triangle_area(3.5, 4)
        self.assertEqual(res, 7)

    def test_perimeter_basic(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = triangle_perimeter(1.5, 2.5, 3)
        self.assertEqual(res, 7)

    def test_perimeter_zero(self):
        res = triangle_perimeter(0, 2, 3)
        self.assertEqual(res, 5)


if __name__ == '__main__':
    unittest.main()
