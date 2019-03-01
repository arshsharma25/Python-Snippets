'''

Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.


There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

'''

r = int(input())
final = []
scorelist = []

for i in range(r):
    name = input()
    score = float(input())
    final.append([name,score])
    scorelist+=[score]
new_scorelist = sorted(list(set(scorelist)))

min = new_scorelist[1]

for name,score in sorted(final):
    if score == min:
        print(name)


