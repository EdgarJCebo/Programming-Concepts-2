#Create functions to validate phone numbers, social security numbers and zip codes using regular expressions. Create a
#main function to get input from a user and then displaying if the phone number, social security number and zip code they entered is valid.
#Be sure to test the functions with various inputs, including valid and invalid examples, to ensure the correctness of the regular expressions.

import re

def validate_phone(phone):
#validates the phone number format that the user needs to insert into the code
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def validate_ssn(ssn):
# validates the social security number format that the user needs to insert into the code
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

def validate_zip(zip_code):
# validates the zip code format that the user needs to insert into the code
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

#asks the user to insert the data
def main():
    print("Please enter the following details:")

    phone = input("Please enter Phone Number (format example: 123-456-7890): ")
    ssn = input("Please enter Social Security Number (format example: 123-45-6789): ")
    zip_code = input("Please enter ZIP Code (format example: 12345 or 12345-6789): ")

#prints results
    print("\nValidation Results:")

    if validate_phone(phone):
        print(f"The phone Number [{phone}] is VALID.")
    else:
        print(f"The phone Number [{phone}] is INVALID.")

    if validate_ssn(ssn):
        print(f"The Social Security Number [{ssn}] is VALID.")
    else:
        print(f"The Social Security Number [{ssn}] is INVALID.")

    if validate_zip(zip_code):
        print(f"The ZIP Code [{zip_code}] is VALID.")
    else:
        print(f"The ZIP Code [{zip_code}] is INVALID.")

if __name__ == "__main__":
    main()