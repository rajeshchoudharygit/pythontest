def task1(tenant_data):
    """Extracting rental data for each customer, converting them into float value and storing in a list"""
    Current_Rent = [float(custdata['Current Rent']) for custdata in tenant_data]
    #Produce a list sorted by “Current Rent” in ascending order
    Current_Rent.sort()
    #Obtain the first 5 items from the resultant list and output to the console
    print(Current_Rent[:5])
    print('\n')
    return Current_Rent[:5]

def task2(tenant_data):
    """create a new list of mast data with “Lease Years” = 25 years"""
    lease_years_25 = [item for item in tenant_data if item['Lease Years'] == '25']
    # calculating the total rent for all tenants with 25 years lease using List Comprehension
    total_rent = sum([float(item['Current Rent']) for item in tenant_data if item['Lease Years'] == '25'])
    count = 1
    #displaying the list of tenants with 25 years lease, inlcuding all data fields
    for each_dict in lease_years_25:
        print(f'Details of tenant number {count} with lease for 25 years \n')
        for key, value in each_dict.items():
            print(key + ' : ' + value)
        count += 1
    #total rent for all tenansts with 25 years lease
    print(f"\nThe total rent for all tenants with 25 years lease is {total_rent}\n")
    return total_rent
