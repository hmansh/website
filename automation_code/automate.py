import os
import re
import sys
import string
import datetime

FILENAME = sys.argv[1]
HTMLFILE = "index.html"

data = ""
try:
    with open('file.txt', 'r') as file:
        data = file.readlines()
except:
    print("Error in Reading Code File")

heading = ""
question = ""
code = ""
codeline = 0

for i, line in enumerate(data):
    if ('!!!heading!!!' in line):
        heading = data[i+1]
        print(data[i+1], end="")
    elif ('!!!question!!!' in line):
        question = data[i+1]
    elif ('!!!code!!!' in line):
        code = ''.join(data[i+1:])
        break;

try : 
    assert(heading != "")
    assert(question != "")
    assert(code != "")
except :
    raise AssertionError

addr = '../Website/code/' + FILENAME + '/' + HTMLFILE

fin = open(addr, "r")
data = fin.read()

if (data == ""):
    raise "Not Enough Data"
try : 
    data = data.replace("_heading_", heading)
    data = data.replace("_question_", question)
    data = data.replace("_code_", code)
    data = data.replace("_date_", str(datetime.datetime.now()))
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