# 💎 Assignment 3: Diamond Pattern

## 📜 Description
Write a Python program to draw a diamond of `*` using loops and string repetition.

## ✨ Example Output
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

## 📌 Guidelines
- 🔺 First, print the upper pyramid (similar to the previous assignment).
- 🔻 Then, print the inverted pyramid below it.
- 🎯 Ensure the diamond remains symmetric.

## 📝 Sample Code Structure
```python
height = 5  # Change this value to modify the diamond size

# Upper pyramid
for i in range(n):
    spaces = ' ' * (n - 1 - i)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# Lower  pyramid
for l in range(n - 1):
    spaces = ' ' * (l + 1)
    stars = '*' * (2 * (n - 1 - l) - 1)
    print(spaces + stars)

```

## 🚀 Instructions
1. 📂 Copy the sample code into a Python file (e.g., `diamond.py`).
2. 🔧 Modify the `height` variable to change the size of the diamond.
3. ▶️ Run the script using Python.
4. 👀 Observe the diamond pattern printed in the console.

## 🎯 Expected Behavior
- ✅ The program should generate a symmetrical diamond.
- 📏 The widest row should be in the center.
- 📌 Each row should be center-aligned using spaces.

## 🔥 Additional Challenge
- 🏗️ Modify the program to accept user input for the height of the diamond.
- 🎨 Try different characters instead of `*` to create custom patterns.

## 🔡 Example with User Input
```python
height = int(input("Enter the height of the diamond: "))

# Upper Pyramid
for i in range(height):
    spaces = ' ' * (height - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# Lower Inverted Pyramid
for i in range(height - 2, -1, -1):
    spaces = ' ' * (height - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)
```

🎉 Happy Coding! 🚀
