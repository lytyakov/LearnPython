import csv

def main():

    fields = ['name', 'age', 'job']

    rows = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
    ]

    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter=',')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    main()