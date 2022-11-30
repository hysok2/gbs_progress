import csv

input = 'gbs_progress.csv'

with open('gbs_progress.csv', encoding='utf8', newline='') as f:
    with open('gbs_progress.md', 'w', encoding='utf8') as f2:
        first = True
        csvreader = csv.reader(f)
        for row in csvreader:
            for c in row:
                f2.write('|' + c )
            f2.write('|\n')
            
            if first:
                f2.write('|:--|:--|:--|\n')
                first = False