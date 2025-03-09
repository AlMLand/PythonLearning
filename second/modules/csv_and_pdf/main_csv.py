import csv
from dataclasses import dataclass, fields


#   built-in library: csv module;
#   external libraries: pandas, openpyxl, google sheets python api

@dataclass
class CsvRow:
    id: int
    first_name: str
    last_name: str
    age: int
    city: str
    email: str


def get_headers():
    return [modify_header_name(field) for field in fields(CsvRow)]


def modify_header_name(field):
    return field.name.replace('_', '').capitalize()


with open('example-read.csv', mode='r', encoding='utf-8') as csv_file_read:
    csv_data = csv.reader(csv_file_read, delimiter=';')
    rows = [CsvRow(int(row[0]), row[1], row[2], int(row[3]), row[4], row[5])
            for index, row in enumerate(csv_data)
            if index > 0]

    with open('example-write.csv', mode='w', encoding='utf-8', newline='') as csv_file_write:
        writer = csv.writer(csv_file_write, delimiter=';')
        writer.writerow(get_headers())
        for row in rows:
            writer.writerow([row.id, row.first_name, row.last_name, row.age, row.city, row.email])
        print('CSV file has been updated')
