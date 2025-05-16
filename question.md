<think>
Okay, I need to create an intermediate-level Python programming assignment based on the provided course material. Let me go through the slides and see what concepts are covered.

The course material includes topics like if statements, Boolean expressions, relational operators, nested ifs, and common errors such as using = instead of ==. There's also mention of scope and variables within blocks.

I should design a problem that uses these concepts. Maybe something where students have to determine the type of triangle based on side lengths. That would require using if-elif-else statements and Boolean conditions.

Let me outline the problem: Given three integers representing the sides of a triangle, classify it as equilateral, isosceles, or scalene. Also, check if it's valid.

I need to ensure that the input is handled correctly. The function should take three arguments. 

First, validate the triangle by checking if any side is zero or negative. Then, sort the sides to make comparisons easier. Using sorted(sides) will help in determining the type without worrying about order.

For classification:
- Equilateral: all sides equal.
- Isosceles: exactly two sides equal.
- Scalene: all sides different.

I should include nested if statements or use elif for efficiency and clarity.

Now, structuring the problem description. The input is three integers, and the output is a string indicating the type and validity.

Sample inputs and outputs would help clarify expectations. For example, 2,2,2 returns "Equilateral triangle", while 3,4,5 returns "Scalene triangle" along with the check for being valid.

I should also mention edge cases like zero or negative values to ensure students handle invalid triangles correctly.

The problem seems solvable using core Python concepts without needing advanced libraries. It reinforces if statements and Boolean logic, aligning well with the course material.
</think>

```
---
**Problem Title:** Triangle Classifier

**Problem Description:**  
Write a function that takes three integers representing the lengths of the sides of a triangle and returns a string indicating whether the triangle is equilateral, isosceles, or scalene. Additionally, check if the given sides can form a valid triangle.

**Input Format:**  
- Three integers representing the lengths of the sides of a triangle.

**Output Format:**  
- A string indicating:
  - "Equilateral triangle" if all sides are equal.
  - "Isosceles triangle" if exactly two sides are equal.
  - "Scalene triangle" if all sides are different.
  - "Not a valid triangle" if the given sides cannot form a triangle.

**Example:**  
_Input:_ 2, 2, 2  
_Output:_ "Equilateral triangle"

_Input:_ 3, 4, 5  
_Output:_ "Scalene triangle" and "Valid triangle"

_Input:_ 0, 1, 2  
_Output:_ "Not a valid triangle"
---

**Solution Code:**
```python
def classify_triangle(a, b, c):
    # Check if any side is invalid
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    
    # Check if the sum of any two sides is greater than the third
    if (a + b > c) and (b + c > a) and (c + a > b):
        # Determine type based on equality
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or c == a:
            return "Isosceles triangle"
        else:
            return "Scalene triangle"
    else:
        return "Not a valid triangle"

# Example usage:
a, b, c = map(int, input().split())
result = classify_triangle(a, b, c)
print(result)
```

**Explanation:**  
1. The function `classify_triangle` first checks if any of the sides are non-positive, returning "Not a valid triangle" if so.
2. It then checks if the given sides can form a valid triangle using the triangle inequality theorem.
3. Based on the equality of the sides, it classifies the triangle as equilateral, isosceles, or scalene.
4. The main program reads three integers from input and prints the result of classification.
```