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


"""
The time complexity of above solution is exponential. In worst case, we may 
end up doing O(3m) operations. The worst case happens when none of characters of
two strings match. Below is a recursive call diagram for worst case.

*********
*********

We can see that many sub problems are solved,again and again, for example,eD(2,2)
is called three times. Since same sub problems are called again, this problem 
has Overlapping Sub problems property. So Edit Distance problem has both 
properties of a dynamic programming problem. Like other typical 
Dynamic Programming (DP) problems, recomputations of same sub problems can 
be avoided by constructing a temporary array that stores results of sub problems.
"""


# A Dynamic Programming based Python program for edit distance problem
def editDistDP(str1, str2, m, n):
    # Create a table to store results of sub problems
    dp = [[0 for x in range(n+1)]for x in range(m+1)]

    # Fill d[] [] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]


# Driver program
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))


