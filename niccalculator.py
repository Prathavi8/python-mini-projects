import datetime

# Funtion for validating user inpput
def validate (nic : str) -> bool:
    nic_number = len(nic)
    if nic_number != 12:
        return False
    else:
        is_digit = nic.isdigit()
        return is_digit

#Funtion for identifing born year
def get_born_year (nic : str) -> int:
    year = nic[0:4]
    return int(year)

# Get born date
def get_born_date (nic : str) -> datetime.date:
    born_day = int(nic[4:7])
    if born_day > 500:
        born_day = born_day - 500
    year = get_born_year(nic)
    jan_first = datetime.date(year,1,1)
    born_year = jan_first + datetime.timedelta(days=born_day - 1)
    return born_year

# Get the NIC as a input from the user
#nic_number = input("Please enter your nic number: ")

# Validate user input
#valid_nic = validate(nic_number)
#if not valid_nic:
    #print("Invaild NIC! Please check the number again")
    #exit(0)

# Identify the born year
#year = get_born_year(nic_number)

# Calculate the exact born day
#born_date = get_born_date(nic_number)

# Print the output
#iso_date = born_date.isoformat()
#print(f'Your Birthday: {iso_date}')
#day = born_date.strftime('%A')
#print(f'Born Day: {day}')