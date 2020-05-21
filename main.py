'''
main file to start execution of the program
'''
from readcsv import read_csv
from preparedata import task1, task2, task3, task4

if __name__ == '__main__':
    tenant_data = read_csv()
    options = ['1', '2', '3', '4']
    while True:
        keyboard_input = input("Please enter 1 to execute task1, 2 for task2, 3 for task3 "
                               "& 4 for task4 or enter 'Exit' to exit: ").strip()
        if keyboard_input in options:
            keyboard_input = int(keyboard_input)
            if keyboard_input == 1:
                print('\n')
                task1(tenant_data)
            elif keyboard_input == 2:
                print('\n')
                task2(tenant_data)
            elif keyboard_input == 3:
                print('\n')
                task3(tenant_data)
            elif keyboard_input == 4:
                print('\n')
                task4(tenant_data)
        elif keyboard_input == 'Exit':
            break
        else:
            print("\nBad input, please select appropriate option \n")
