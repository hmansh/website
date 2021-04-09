#!/bin/bash

file=$(ls ../Website/code/ | wc -l)
mkdir ../Website/code/code_$file
cp ../Website/code/code-template.html ../Website/code/code_$file/index.html
python3 automate.py code_$file
python3 updateHome.py code_$file
cd ../website/
git add .
git commit -m 'updated_$(file)'
git push