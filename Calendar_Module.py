'''
You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August th  was WEDNESDAY.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

D = list(map(int,input().split()))

d = D[1]
m = D[0]
y = D[2]

def switch(v):
    switcher = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
    for key,val in switcher.items():
        if key == v:
            return val

val = switch(calendar.weekday(y,m,d))

print(val)

