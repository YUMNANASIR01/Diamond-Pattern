
n = 5  # Number of rows for the upper half of the diamond
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


