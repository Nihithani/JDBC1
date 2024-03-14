import datetime

#create a date object representing current date
current_date = datetime.date.today()

#print the current date
print(current_date)

#create the date obj repr specific date
specific_date = datetime.date(2023,5,15)
print(specific_date)

#calc diff btwn 2 dates
date1 = datetime.date(2023,5,15)
date2 = datetime.date(2023,5,30)
date_diff = date2-date1
print("Difference in date time" ,date_diff.days, "days")


#formatted datetime
for_dt = specific_date.strftime("%Y-%m-%d %H:%M:%S")


#print a formatted string time date
print(for_dt)

#parsed date time object
par_st= datetime.datetime.strptime("2023-05-15 10:30:00", "%Y-%m-%d %H:%M:%S")
print(par_st)







#for formatting we use m for full month name display and M for number
print("year",now.strftime(%Y))
print("2 digit year",now.strftime(%y))
print("month in number",now.strftime(%m))
print("month in abbreviation",now.strftime(%b))
print("month in full name",now.strftime(%B))
print("day of month",now.strftime(%d))
print("day of week in number",now.strftime(%a))
print("day of week in abbreviation",now.strftime(%A))



import re

text = "The quick brown fox jumps over the lazy dog"

#1- re.match()  whether the given text starts with the pattern or not
pattern1 = r"The" #define a pattern
match1 = re.match(pattern1,text) #attempt to match the pattern i.e it returns false
print("re.match():" ,match1.group() if match1 else "no match")

#2- re.search(): search for a pattern anywhere in the string
pattern2 = r"Brown"
match2 = re.search(pattern2,text) #search for the pattern anywhere in the string
print("re.search()",match2.group() if match2 else "No match")

#3- re.findall(): find all occurances of a pattern in a string
pattern3= r"o\w"











import re
text =  "The quick brown fox jumps over the lazy dog"
#1. .(dot): matches any single character except new line
pat1 = r"b..wn" #define any pattern to match
match1 = re.search(pat1,text)
print(pat1)
print(match1.group() if match1 else "no match")

#2. ^ (caret): matches the start of the string
pattern2 = r"^The" #define any pattern to match start of string
match2 = re.search(pattern2,text)
print(pattern2)
print(match2.group() if match2 else "no match")

#3. $ (dollar): matches the end of the string
pattern3 = r"dog$" #define any pattern to match end of string
match3 = re.search(pattern3,text)
print(pattern3)
print(match3.group() if match3 else "no match")

#4. \ (backslash): Escapes special characters or indicates a special sequence
pattern4 = r"\s" #define any pattern to match witespace character
match4 = re.findall(pattern4,text)
print(pattern4)
print("matches found", match4) # output - [' ', ' ', ' ',' ', ' ', ' ']

#5. [] (square brackets): specifies a character class, matches any one of the the enclosed characters
pattern5 = r"[aeiou]" #define a pattern to match any vowel
matches5 = re.findall(pattern5,text)
print(pattern5)
print(matches5)