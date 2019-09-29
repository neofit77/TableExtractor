This is python project for extract table from jpg, png or pdf files to csv file.

Requirements:
- Python3 (I tested with version 3.6)
- Python library wand 

Instruction:
- Add to the folder "allFiles" the files from which you want to extract the tables
- In the terminal, go to the project folder and then type "python3 start.py"
- Wait a few minutes (depending on the number of files you have saved in the folder 'allFiles')
- When you see in the terminal that the program is finished:
  - in the image folder you will have inverted pdf files into images and existing jpg and png files, 
  - in the jsonFiles folder you will have all the files in json format 
  - in the csvFiles folder you will have csv files with tables.
  
  NOTE:
  The program uses the API from https://extracttable.com/ so that some accuracy 
  in extract tables depends on this web application.
  
  Enjoy!

