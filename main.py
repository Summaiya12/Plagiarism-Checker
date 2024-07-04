from difflib import SequenceMatcher

with open('adapter.txt') as file_1,open('add.txt') as file_2:
   file_1_data = file_1.read()
   file_2_data = file_2.read()
   similarity = SequenceMatcher(None,file_1_data,file_2_data).ratio()
   print("The plagiarism checker of both files is",similarity*100)