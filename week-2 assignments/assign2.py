import re
f = open("D:\Python-Coursera\week-2 assignments\etest_data_assignment2.txt", "r")
x = re.findall("[0-9]+", f.read())
sum1 = 0
for i in x:
    num = int(i)
    sum1 = sum1 + num

print(sum1)