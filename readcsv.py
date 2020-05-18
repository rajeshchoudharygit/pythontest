import csv


def read_csv():
    """read data from csv file, make a list of dictionary from the data and return list to the caller"""
    csv.register_dialect('myDialect',
                         delimiter=',',
                         quoting=csv.QUOTE_ALL)
    tenant_data = []
    with open('./testdata/Python Developer Test Dataset.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file,  dialect='myDialect')
        for row in csv_reader:
            tenant_data.append(row)
    return tenant_data