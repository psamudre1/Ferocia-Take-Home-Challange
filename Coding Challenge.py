# Asks user to input their investment term in months
while True: 
    try:
        investment_term = float(input("How many months will you be investing: "))
    # In the event a non-numerical value is input, user will be asked to reattempt    
    except ValueError:
        print("Please enter a numerical value for the amount of months you will be investing")
        continue
    # In the event a negative value is input, user will be asked to reattempt as investment term can only be positive
    if investment_term <= 0:
        print("Please enter a value greater than 0")
        continue 
    # When value input correctly, the investment term will be accepted and loop will end 
    else: 
        break

# Asks user to input their staring deposit
while True: 
    try:
        principal = float(input("What is your starting deposit in dollar figures: "))
    # In the event a non-numerical value is input, user will be asked to reattempt 
    except ValueError:
        print("Please enter a numerical value for your starting deposit (No need for ($) sign")
        continue
    # In the event a negative/zero value is input, user will be asked to reattempt as starting deposit can only be positive
    if principal <= 0:
        print("Please enter a value greater than 0")
        continue
    # When value input correctly, the starting deposit will be accepted and loop will end  
    else: 
        break


# Dictionary that represents how often interest is credited in a month for each term
# This is in terms of a month, as the investment period collected earlier is also in terms of months 
dict ={1:1.0, 2:1/3.0, 3:1/12.0, 4:1/investment_term}

# Represnets the rate of compounding
# Will be used at the end to provide a clear depiction of all the inputs
dict_names = {1:"Monthly",2:"Quaterly",3:"Yearly",4:"At maturity"}

# Asks user to clarify how often interest is being paid
while True: 
    try:
        interest_paid = int(input("""
        How often is interest being paid (select a number between 1-4)
        1. Monthly 
        2. Quaterly 
        3. Yearly 
        4. At maturity 
        """))
    # In the event a non-numerical value is input, user will be asked to reattempt 
    except ValueError: 
        print("Please enter a number between (1-4) representing how often interest is paid")
        continue
    # In the event a number that does not represent any interest paid is input, user will be asked to reattempt
    if interest_paid not in dict:
        print("Please enter a number between (1-4) representing how often interest is paid")
        continue
    # User successfully inputs a number between 1-4, then loop will end 
    else:
        break



# How often the chosen interest paid frequenct is applied every month
interest_paid_in_months = dict[interest_paid]


# Asks user to input the annual interest rate
while True: 
    try:
        interest_rate_percent = float(input("What is your annual interest rate (input as a percentage): "))
    # In the event a non-numerical value is input, user will be asked to reattempt 
    except ValueError:
        print("Please enter a percentage value (no need for the percent symbol) ")
        continue
    # Interest rate must be positive or equal to 0, it cannot be negative. 
    # If a negative value is input, then user will be asked to reattempt
    if interest_rate_percent < 0:
        print("Please enter a value greater than or equal to 0")
        continue 
    else: 
        break

# Annual rate must be converted into monthly rate, as other variables are in terms of months
interest_rate_decimal_permonth = (interest_rate_percent/(100*12))


# Final formula in order to calculate final balance 
def term_deposit_calculator(interest_paid_in_months, investment_term, interest_rate_decimal_permonth,principal):


    final_value = principal*(1+(interest_rate_decimal_permonth/interest_paid_in_months))**(interest_paid_in_months*investment_term)
    return  final_value

print(f"A starting balance of ${round(principal,2)} invested over {investment_term} months at an interest rate of {interest_rate_percent}% p.a. with interest being paid {dict_names[interest_paid]} will yield a final balance of ${round(term_deposit_calculator(interest_paid_in_months, investment_term, interest_rate_decimal_permonth, principal),2)}")