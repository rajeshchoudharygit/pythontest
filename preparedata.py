'''
Module to work on tasks and print output to the console.
'''
import math
import re
import datetime


def task1(tenant_data):
    """Extracting rental data for each customer,
     converting them into float value and storing in a list"""
    current_rent = [float(custdata['Current Rent']) for custdata in tenant_data]
    #Produce a list sorted by “Current Rent” in ascending order
    current_rent.sort()
    #Obtain the first 5 items from the resultant list and output to the console
    print(current_rent[:5])
    print('\n')
    return current_rent[:5] # to validate test case

def task2(tenant_data):
    """create a new list of mast data with “Lease Years” = 25 years"""
    lease_years_25 = [item for item in tenant_data if item['Lease Years'] == '25']
    # calculating the total rent for all tenants with 25 years lease using List Comprehension
    total_rent = sum([float(item['Current Rent']) for
                      item in tenant_data if item['Lease Years'] == '25'])
    count = 1
    #displaying the list of tenants with 25 years lease, inlcuding all data fields
    for each_dict in lease_years_25:
        print(f'Details of tenant number {count} with lease for 25 years \n')
        for key, value in each_dict.items():
            print(key + ' : ' + value)
        count += 1
    #total rent for all tenansts with 25 years lease
    print(f"\nThe total rent for all tenants with 25 years lease is {total_rent}\n")
    return total_rent  #to validate test case


def task3(tenant_data):
    """Create a dictionary  containing tenant name and a count of masts for each tenant"""
    # list containing all the entries of tenants name in the Tenant Name column
    tenants = [tenantdata['Tenant Name'] for tenantdata in tenant_data]
    #looping through all the entries of tenants list starting from 0 index
    each_tenant = tenants[0]
    distinct_tenants = 1
    while True:
        search_length = math.floor(len(each_tenant) / 3)#calculating 1/3 size of the tenant's name
        # making a substring that would be used to find matches
        match_text = each_tenant[:search_length]
        # using regular expression to form a match_text
        regular_expression = re.compile(f".*{match_text}*")
        # finding match for match_text in tenants list and storing in newlist
        newlist = list(filter(regular_expression.match, tenants))
        #removing matched data from original list to avoid duplicates
        tenants = [ele for ele in tenants if ele not in newlist]
        print(f"{each_tenant} have a mast count of {len(newlist)}\n")
        if len(tenants) == 0:
            break
        each_tenant = tenants[0]
        distinct_tenants += 1
    return distinct_tenants#to validate test case


def task4(tenant_data):
    """List the data for rentals with “Lease Start Date” between
    1st June 1999 and 31st August 2007"""
    #lease_start_date = [item for item in tenant_data
    # if (01-June-99<= item['Lease Start Date'] <=31-August-07]
    format_str = '%d %b %Y'  # current date format as a string
    lease_year_date = []
    start_date = datetime.date(1999, 6, 1)  # desired lease start date between between 1st June 1999
    end_date = datetime.date(2007, 8, 31) # and 31st August 2007
    for each_item in tenant_data:
        # converting lease start date from string to datetime object
        # and then comparing again desired start date
        datetime_obj = datetime.datetime.strptime(each_item['Lease Start Date'], format_str)
        if start_date <= datetime_obj.date() <= end_date:
            #formatting date for all the string entries used in lease end date and lease start date
            each_item['Lease Start Date'] = datetime_obj.strftime("%d/%m/%Y")
            each_item['Lease End Date'] = datetime.datetime.strptime\
                (each_item['Lease End Date'], format_str).strftime("%d/%m/%Y")
            lease_year_date.append(each_item)
            #iterating through the selected entries and displaying on console
            for key, value in each_item.items():
                print(key + ' : ' + value)

            print('\n')
    return len(lease_year_date) #to validate test case
