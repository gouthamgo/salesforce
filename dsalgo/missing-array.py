"""
Missing in Array
Difficulty: EasyAccuracy

You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size() + 1



    The sum of the first n natural numbers is given by the formula (n * (n + 1)) / 2. The idea is to compute this sum and subtract the sum of all elements in the array from it to get the missing number.

    def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))



    n = 4 + 1 ==> 5 

    i  => 1 till 6 
    flag 
    j - 0 till 4
    

"""

# i got an array 

def missingElement(arr):
    n = len(arr)+1

    total = sum(arr)

    exceptedSum = n *(n+1)//2

    return exceptedSum - total









print(missingElement([8, 2, 4, 5, 3, 7, 1]))




