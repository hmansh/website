import os
import re
import sys
import string
import datetime
import calendar

FILENAME = sys.argv[1]
HTMLFILE = "index.html"

data = ""
try:
    with open('file.txt', 'r') as file:
        data = file.readlines()
except:
    print("Error in Reading Code File")

heading = ""

for i, line in enumerate(data):
    if ('!!!heading!!!' in line):
        heading = data[i+1]
        print(data[i+1], end="")
        break;

try : 
    assert(heading != "")
except :
    raise AssertionError

addr = '../Website/' + HTMLFILE

fin = open(addr, "r")
data = fin.read()
count = 4;
day = datetime.date.today().day
month = calendar.month_name[datetime.date.today().month]

title = f'''
            <li><p>{day} {month} | </p><a href="code/{FILENAME}/index.html">{heading}</a></li>
            <!--insert_here-->
        '''

if (data == ""):
    raise "Not Enough Data"
try : 
    data = data.replace("<!--insert_here-->", title)
    fin.close()
except : 
    raise "Data Replacement Failed"

try : 
    fin = open(addr, "wt")
    fin.write(data)
    fin.close()
except :
    FileExistsError

print("Completed!")