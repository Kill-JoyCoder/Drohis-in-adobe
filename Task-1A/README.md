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
- os: reading into a pdf and writing out the json 


## Running with Docker (Recommended)
a. Build the Docker Image

Open your terminal (Command Prompt or PowerShell on Windows) and run:

docker build -t task-1a:latest .

b. Prepare Folders for Input/Output Place your input PDF files in the input/ directory at your project root.

Ensure there is an outputs/ directory for results. If there is none, the program will create a new output/ directory.

c. Run in Interactive Mode (Prompts for Persona & Job)

docker run --rm -it -v %cd%\pdfs:/app/pdfs -v %cd%\outputs:/app/outputs task-1a:latest

## Running via python
a. Drop the documents to classify
Ensure you use the input/ directory for this.

b. Using your terminal of choice, go to the root directory of this repo

cd C:/Users/<user>/..../Drohis-in-adobe/Task-1A

Then use

python3 main.py 

The terminal will display some prompts after each document is done processing.
Check the output/ directory for the respective .json files
