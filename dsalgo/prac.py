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




        





