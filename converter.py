import csv  
import json 

with open('wildberries.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('wb.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f)