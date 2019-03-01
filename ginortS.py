'''

You are given a string S. 
 contains alphanumeric characters only. 
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input
Sorting1234

Sample Output
ginortS1324

'''

string = input()

string_list = []
digit_list = []
str_len = len(string)

for i in range(str_len):
    if string[i].isalpha():
        string_list.append(string[i])
    elif string[i].isdigit():
        digit_list.append(string[i])

string_lower = []
string_upper = []

for val in string_list:
    if val.islower():
        string_lower.append(val)
    else:
        string_upper.append(val)


updated_string = sorted(string_lower) + sorted(string_upper)

odd_list = []
even_list = []
for val in digit_list:
    if int(val)%2==0:
        even_list.append(int(val))
    else:
        odd_list.append(int(val))
        
odd_list = sorted(odd_list)
even_list = sorted(even_list)

updated_digit = odd_list + even_list

new_updated_digit = [str(val) for val in updated_digit]


s = ''

s = s.join(updated_string)


f = ''
f = f.join(new_updated_digit)

final_string =  s + f

print(final_string)

