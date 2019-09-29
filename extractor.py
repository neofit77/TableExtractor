import json
import csv
from pathlib import Path

dir_path = Path('jsonFiles')
csv_path = Path('csvFiiles')
files = dir_path.iterdir()

for file in files:
    name=file.name[:-5]
    with open(dir_path/file.name,'r') as f:
        JS= json.load(f) #load json file
        num_tables = len(JS["Tables"]) # number of tables

    for table in range(num_tables):
        if num_tables>1:
            nameCSV = '{}_Table_{}.csv'.format(name,table+1)
        else:
            nameCSV = '{}.csv'.format(name)

        with open(csv_path/nameCSV,'w') as f:
            num_rows = len(JS['Tables'][table]['TableJson'])
            for i in range(num_rows):
                csvFile = csv.writer(f)
                csvFile.writerow(JS["Tables"][table]['TableJson'][str(i)].values())



