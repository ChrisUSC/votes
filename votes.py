states = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 55,
    "Colorado": 9,
    "Connecticut": 7,
    "Delaware": 3,
    "DC": 3,
    "Florida": 29,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 20,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas": 6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine Pop": 2,
    "Maine 1": 1,
    "Maine 2": 1,
    "Maryland": 10,
    "Massachusetts": 11,
    "Michigan": 16,
    "Minnesota": 10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana": 3,
    "Nebraska Pop": 2,
    "Nebraska 1": 1,
    "Nebraska 2": 1,
    "Nebraska 3": 1,
    "Nevada": 6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico": 5,
    "New York": 29,
    "North Carolina": 15,
    "North Dakota": 3,
    "Ohio": 18,
    "Oklahoma": 7,
    "Oregon": 7,
    "Pennsylvania": 20,
    "Rhode Island": 4,
    "South Carolina": 9,
    "South Dakota": 3,
    "Tennessee": 11,
    "Texas": 38,
    "Utah": 6,
    "Vermont": 3,
    "Virginia": 13,
    "Washington": 12,
    "West Virginia": 5,
    "Wisconsin": 10,
    "Wyoming": 3
}

# Python3 program to prdistinct subset
# Sums of a given array.

# Uses Dynamic Programming to find
# distinct subset Sums
# adapted from: https://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/
# This code is contributed
# by mohit kumar
def getDistSum(arr, n):

    Sum = sum(arr)

    # dp[i][j] would be true if arr[0..i-1]
    # has a subset with Sum equal to j.
    dp = [[False for i in range(Sum + 1)]
                for i in range(n + 1)]

    # There is always a subset with 0 Sum
    for i in range(n + 1):
        dp[i][0] = True

    # Fill dp[][] in bottom up manner
    for i in range(1, n + 1):

        dp[i][arr[i - 1]] = True

        for j in range(1, Sum + 1):

            # Sums that were achievable
            # without current array element
            if (dp[i - 1][j] == True):
                dp[i][j] = True
                dp[i][j + arr[i - 1]] = True

    # Print last row elements
    result = []
    for j in range(Sum + 1):
        if (dp[n][j] == True):
            result.append(j)

    return result

# Driver code
arr = list(states.values())
n = len(arr)
sums = getDistSum(arr, n)

# prints the list of all unique possible elector sums
print(sums)
# prints True if the 'sums' varaible is equal to the range [0...538]
print(sums == list(range(539)))
