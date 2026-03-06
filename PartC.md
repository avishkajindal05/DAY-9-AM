Q1 Conceptual
Explain the difference between:

Shallow Copy
Deep Copy
Include:

Example with nested lists
Why shallow copy fails
When deep copy is required


> shallow copy :
A shallow copy creates a new outer object, but the inner objects are still referenced from the original object.
This means the top-level list has a different memory address, but the nested elements point to the same inner objects.
If the nested objects are modified, the changes will appear in both lists.
eg: import copy

original = [[1,2,3], [4,5,6]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original)
print(shallow)

output: [[99,2,3], [4,5,6]]
[[99,2,3], [4,5,6]]

Why Shallow Copy Fails:
Shallow copy fails when working with nested mutable structures such as:
lists inside lists
dictionaries inside lists
objects containing other objects
Since the inner objects are not copied, modifying them affects both the original and the copied structure.

>Deep copy: 
A deep copy creates a completely independent copy of the object, including all nested objects.
Every level of the structure gets a new memory reference.
Changes in the copied structure do not affect the original object.
e.g.: import copy

original = [[1,2,3], [4,5,6]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)
print(deep)

output: [[1,2,3], [4,5,6]]
[[99,2,3], [4,5,6]]


Q2 Coding — List Rotation
Write a function:

rotate_list(lst, k)
Example:

rotate_list([1,2,3,4,5], 2)
Output:

[4,5,1,2,3]
Requirements:

Use list slicing
Handle k > len(lst)

>> def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst
    k = k % n      # handles k > len(lst)
    return lst[-k:] + lst[:-k]
print(rotate_list([1,2,3,4,5], 2))



Q3 Debug Problem
Find the bug in this code.

nums = [1, 2, 3, 4, 5, 6, 7, 8]

for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print(nums)
Expected output:

[1,3,5,7]
Hint:

Try running with:

[2,4,6,8]
Explain:

Why the bug happens
Provide a correct solution

>> nums = [1,2,3,4,5,6,7,8]

for num in nums[:]:
    if num % 2 == 0:
        nums.remove(num)

print(nums)