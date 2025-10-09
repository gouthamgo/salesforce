print(f"Begin here")
# f lets us put variables inside strings 

# list
sizes = [10,20, 8,24,20]

print(len(sizes))

# for i in range(5):
#     print(i)

# count = 0 

# while count < 5:
#     print(count)
#     count +=1




word = "hello"
freq = {}

# for letter in word:
#     if letter in freq:
#         freq[letter] +=1
#     else:
#         freq[letter]=1

for letter in word:
    freq[letter] = freq.get(letter,0) +1 
    # give me the value of the letter or 0 if it doesnt exist yet 

print(freq)


#  go through each letter in word and if that letter is in freq dict +1 or else is 1 




nums = [1,2,3,2,4,5,3,6]

freq1={}

for num in nums:
    freq1[num] = freq1.get(num,0)+1
print(freq1.items())


duplicates = []
for num,count in freq1.items():
    if count > 1:
        duplicates.append(num)
print(duplicates)



numbers = [5,12,8,130,44,15,8,5]

# need to find nums that appear more than once

freq ={}

for num in numbers:
    freq[num] = freq.get(num,0)+1

dups = []

for num,count in freq.items():
    if count >1:
        dups.append(num)
print(dups)

biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num


print(biggest)

count=0

for num in numbers:
    if num >10:
        count +=1
print(count)

#  hashmap for counting 
# loop and conditional counting 

nums = [2,7,11,15] 
target = 9


def findtarget(nums,target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+ nums[j] == target:
                return [i,j]
            

print(findtarget(nums,target))



nums = [2,7,11,15] 
target = 9

seen = {}

# for i,num in enumerate(nums):
#     needed = target - num

#     if needed in seen:
#         return[seen[needed],i]
    
#     seen[num] = i

for i,num in enumerate(nums):
    print(f"Index {i}: value {num}")
# enumerate gives both index and value at the same time 


#  so basically 

def two_sum(nums,target):

    seen = {}

    for i,num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return (seen[needed],i)
        
        seen[num] = i 




print(two_sum([2,7,11,15],9))

# ===================================================

nums = [1,2,3,1]

def containsDup(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0)+1
    
    for i,count in freq.items():
        if count >1:
            return True
        
    return False





print(containsDup([1,2,3,1]))



def containes_duplicate(nums):

    seen ={}

    for num in nums:
        if num in seen: 
            return True
        seen[num] = True
    return False

# =========================================================

max_p = 0
prices = [7,1,5,3,6,4]

for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        profit = prices[j] - prices[i]
        max_p = max(max_p,profit)
print(max_p)



def best_price(prices):

    low = prices[0]
    best = 0


    for price in prices:
        if price < low:
            low = price
        
        profit = price - low

        if profit > best:
            best = profit
    return best
    
print(f" best + {best_price([7,1,5,3,6,4])}")




        



# ================================

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109



'''

# print(([1,2,3] + [2,5,6]))


# def check(nums1, nums2, m, n):

#     # 1 2 3 --- 2 5 6 




nums1 = [1,2,3]
nums2 = [2,5,6]

merge = []
i, j = 0, 0  # pointers for nums1 and nums2

while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        merge.append(nums1[i])
        i += 1
    else:
        merge.append(nums2[j])
        j += 1

# One of the lists might still have elements left
merge.extend(nums1[i:])
merge.extend(nums2[j:])

print(merge)  # Output: [1, 2, 2, 3, 5, 6]









# ===========================================================


def is_valid(s):
    matches = {
        ')': '(',
        '}':'{',
        ']':'['
    }

    stack =[]

    for char in s:
        if char in matches:
            if len(stack) == 0:
                return False
            if stack[-1] == matches[char]:
                stack.pop()
            else: 
                return False
        else:
            stack.append(char)
    return len(stack) == 0

#  basically we check if the stack has anything or not , compare with the last element







# ===============================


'''
Majority Element 
Given an array --> find the element that appears more than n/2 times 

think > check if something is bigger than len(nums)/2 ==> pattern to remember 
'''

def majority(nums):

    count = {}

    for num in nums:
        count[num] = count.get(num,0)+1
    
    print(count)

    for num,freq in count.items():
        print(freq)
        if freq > len(nums)/ 2:
            return num
 


print(majority([3,2,3]))


'''
Missing number 
Given an array containing n disctinct numbers from 0 to n --> find the missing number 

pattern ==>
'''

def missing(arr):
    





print(missing([3,0,1]))




















# ====================================================


'''
Opps --> organises code into objects - represents real world entities each containing data (attributes) and behaviour(method)

Abstraction, Encapsulation , Classes , Objects, Inheritance, Polymoirphism 

Time COmplexity --> describes the amount of time necessary to execute an algorithm

Space Complexity  --> describes amount of memory or space utilized by an algorithm / program  

Big O -- helps us understand how the performance of an algorithm changes as the size of the input grows , providing a simple way to compare and analyse different algorithm's efficiency 


O(1) --> Constant --> time taken remains constant regardless of input size 

O(logn N) --> Logarithmic --> Time taken increases logarithmically as input size grows. Operations are typically halved at each step. Time increases linearly as N goes up exponentially. 

O(N) --> Linear

O(N log N) --> Linearithmic

O(N ^2) --> Quadratic 

O(2^N) --> exponential

O(N!) --> Factorial 

'''









