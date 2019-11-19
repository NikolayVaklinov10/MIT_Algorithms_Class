"""
Edit Distance:

Given two str1 and str2 and below operations that can perform on str1.
Find minimum number of edits (operations) required to convert 'str1'
into 'str2'

1. Insert
2. Remove
3. Replace

m: Length of str1 (first string)
n: Length of str2 (second string)
"""

# A Naive recursive Python program to find minimum operations to
# convert str1 to str2
def editDistance(str1, str2, m, n):

    # If first string is empty, the only option is to insert all
    # characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing much to do.
    # Ignore last characters and get count for remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    # If last characters are not same, consider all three operations
    # on last character of first string, recursively compute minimum cost for
    # all three operations and take minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n-1),     # Insert
                   editDistance(str1, str2, m-1, n),     # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )

# Driver program to test the above function
str1 = "sunday"
str2 = "saturday"
print(editDistance(str1, str2, len(str1), len(str2)))





