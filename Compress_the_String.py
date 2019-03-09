'''
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
'''

from itertools import groupby

for var,rep in groupby(input()):
    print((len(list(rep)),int(var)), end = ' ')


# or

my_input = input()

count = 1
for i in range(len(my_input)):
    try:
        if my_input[i] == my_input[i+1]:
            count += 1
        else:
            print((count, int(my_input[i])), end=" ")
            count = 1
    except IndexError:
        print((count, int(my_input[i])))
