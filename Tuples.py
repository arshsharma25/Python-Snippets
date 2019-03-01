'''

Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple. 
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t)


Sample Input 0
2
1 2

Sample Output 0
3713081631934410656

'''

r = input()
v = input()

t1 = v.split()
t1 = [int(x) for x in t1]

t1 = tuple(t1)

print(hash(t1))
