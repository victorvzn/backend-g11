import csv

def showInfo():
    csv_file = open('data.csv', 'r', encoding='utf-8')

    output = csv.reader(csv_file, delimiter=';')

    for reg in output:
        print(reg)
    
    csv_file.close()

    del csv_file

showInfo()
