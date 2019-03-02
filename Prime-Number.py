'''

You are given an integer N. You need to print the series of all prime numbers till N.

Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

Output Format

Print the desired output in single line separated by spaces.

Constraints

1<=N<=1000

'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())

def isPrime(var):
    flag = 0
    for i in range(2,var):
        if var%i == 0:
            flag = 1
            break
    
    if flag == 0:
        return True

for i in range(2,N):
    if isPrime(i):
        print(i, end=" ")


