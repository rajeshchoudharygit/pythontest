from readcsv import read_csv
from preparedata import task1

if __name__ == '__main__':
    tenant_data = read_csv()
    print(tenant_data)
    task1(tenant_data)
