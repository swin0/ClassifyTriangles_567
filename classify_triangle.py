#Sydney Winstead
#SSW 567 HW 00b: Testing Triangle Classification Homework
#1/28/2026
#I pledge my honor that I have abided by the Stevens Honor System.

def classify_triangle(a, b, c):

    #This program classifies a triangle based on its side lengths.
    #Parameters:
    # a (float): Length of side a.
    # b (float): Length of side b.
    # c (float): Length of side c.
    #Prints a string of the classification of the triangle.

    # Validate input: all values must be int/float and greater than 0.
    if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
        return "Invalid Triangle"

    # Sort the sides so that c is the largest.
    sides = sorted([a, b, c])
    a, b, c = sides

    # Triangle Inequality Theorem Check: sum of two smaller sides must be greater than the largest.
    if a + b <= c:
        return "Invalid Triangle"

    # Determine triangle type.
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check if the triangle is a right triangle using the Pythagorean theorem.
    # Rounding is used to avoid floating-point precision issues.
    if round(a**2 + b**2, 5) == round(c**2, 5):
        return f"{triangle_type} Right Triangle"

    return f"{triangle_type} Triangle"

# The block below will only run when the file is executed directly.
# Does not interfere with the unit tests.
if __name__ == '__main__':
    try:
        # Asks user for three side lengths.
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        
        # Classify the triangle and print the result.
        result = classify_triangle(side1, side2, side3)
        print(f"The triangle is classified as: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for the sides.")
