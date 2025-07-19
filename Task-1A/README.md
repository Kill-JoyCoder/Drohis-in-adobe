# Task 1A: Processing pdfs

## Overview 
This implementation aims at providing the structure of a pdf which is then written out into a json file. The input pdfs are moved into the "Task-1A/input" folder. The program uses the text size as a heuristic to confirm the type of heading used in each page and extract the relevant information 

## Solution

### Tech Stack
- Python 

### Libraries
- PyMuPDF: extracts PDF metadata to get text size 
- glob: to recognise all pdf files present in Task-1A/input
- json: for relevant output json format

