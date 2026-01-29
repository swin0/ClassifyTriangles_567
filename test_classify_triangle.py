#Sydney Winstead
#SSW 567 Test Cases for HW 00b Homework
#1/28/2026
#I pledge my honor that I have abided by the Stevens Honor System.

import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        # Test for an equilateral triangle where all sides are equal.
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")

    def test_isosceles_triangle(self):
        # Test for an isosceles triangle where exactly two sides are equal.
        # These tests account for different orders of side lengths.
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles Triangle")
        self.assertEqual(classify_triangle(3, 5, 5), "Isosceles Triangle")
        self.assertEqual(classify_triangle(5, 3, 5), "Isosceles Triangle")

    def test_scalene_triangle(self):
        # Test for a scalene triangle where all three sides are of different lengths.
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene Triangle")

    def test_right_triangle(self):
        # Test for a scalene right triangle where sides follow the Pythagorean theorem.
        # Below are three common Pythagorean triples.
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right Triangle")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Right Triangle")
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene Right Triangle")

    def test_isosceles_right_triangle(self):
        # Test for an isosceles right triangle.
        # In an isosceles right triangle, the legs are equal, and the hypotenuse is leg*sqrt(2).
        self.assertEqual(classify_triangle(1, 1, 2**0.5), "Isosceles Right Triangle")

    def test_invalid_triangle(self):
        # Test cases for invalid triangles where the sides do not satisfy the triangle inequality theorem.
        self.assertEqual(classify_triangle(1, 2, 3), "Invalid Triangle")
        self.assertEqual(classify_triangle(5, 1, 1), "Invalid Triangle")

    def test_edge_cases(self):
        # Test for edge cases:
        # Zero-length side should return "Invalid Triangle"
        self.assertEqual(classify_triangle(0, 5, 5), "Invalid Triangle")
        # Negative side length should return "Invalid Triangle"
        self.assertEqual(classify_triangle(-3, 4, 5), "Invalid Triangle")
        # Non-numeric input should return "Invalid Triangle"
        self.assertEqual(classify_triangle(3, "a", 5), "Invalid Triangle")

if __name__ == '__main__':
    unittest.main()
