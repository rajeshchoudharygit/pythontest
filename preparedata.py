def task1(tenant_data):
    """Extracting rental data for each customer, converting them into float value and storing in a list"""
    Current_Rent = [float(custdata['Current Rent']) for custdata in tenant_data]
    #Produce a list sorted by “Current Rent” in ascending order
    Current_Rent.sort()
    #Obtain the first 5 items from the resultant list and output to the console
    print(Current_Rent[:5])
    print('\n')
    return Current_Rent[:5]
