# coding: utf-8

# custom function for console output formatting
def line_break(repeats, space_location="none"):
    if space_location == "before":
        print(f"\n{'-' * repeats}")
    elif space_location == "after":
        print(f"{'-' * repeats}\n")
    else:
        print(f"{'-' * repeats}")

# import necessary libraries
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
# provided list of loan values
loan_costs = [500, 600, 200, 1000, 450]

# console output formatting
line_break(50,"before")
print(f"Part 1: Automate the Calculations\n")

# count the number of loans in the list
total_number_of_loans = len(loan_costs)

# print output to console
print(f"Total number of loans: {total_number_of_loans}")

# sum the total value of all loan values
sum_of_loan_values = sum(loan_costs)

# print output to console
print(f"Total value of the loans: $ {sum_of_loan_values:,.2f}")

# calculate the average loan amount
average_loan_amount = sum_of_loan_values / total_number_of_loans

# print output to console
print(f"Average loan amount: $ {average_loan_amount:,.2f}")

# console output formatting
line_break(50,"before")

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# provided dict of loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# console output formatting
print(f"Part 2: Analyze the Data\n")

# assign future_value/remaining_months from loan dict to variables
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# print output to console
print(f"Future value of the loan: $ {future_value:,.2f}\nRemaining months on the loan: {remaining_months}")

# assign provided discount rate value of 0.20 to variable
minimum_required_return = 0.2

# calculate present value and assign to variable
loan_fair_value = future_value / (1 + minimum_required_return/12) ** remaining_months

# print output to console
print(f"Calculated fair value (npv) of the loan: $ {loan_fair_value:,.2f}")

# assign loan_price dict value to variable
loan_price = loan.get("loan_price")

# establish output message for loan purchase decision
loan_message = "At a purchase price of $ "

# conditional comparing calculated fair value to loan price for loan purchase decision.
if loan_fair_value >= loan_price:
    # append worthwhile loan purchase analysis to loan_message for console output
    loan_message += str(f"{loan_price:,.2f}, the loan is worth at least the cost to buy it.")
else:
    # append too expensive loan purchase analysis to loan_message for console output
    loan_message += str(f"{loan_price:,.2f}, the loan is too expensive and not worth the price.")

# print fully constructed loan purchase analysis to console
print(f"{loan_message}\n")

# console output formatting
line_break(50)

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# provided dict of new loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# console output formatting
print(f"Part 3: Perform Financial Calculations\n")

# define function for calculating loan npv
def calculate_fair_value(future_value, annual_discount_rate, remaining_months):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months
    return present_value

# assign future value from new loan dict to variable
future_value = new_loan.get("future_value")

# assign provided discount rate value of 0.2 to variable
annual_discount_rate = 0.2

# assign remaining months from new loan dict to variable
remaining_months = new_loan.get("remaining_months")

# calculate new loan npv using the newly written function
present_value = calculate_fair_value(future_value, annual_discount_rate, remaining_months)

# print to console
print(f"The present value of the loan is: $ {present_value:,.2f}")

# console output formatting
line_break(50,'before')

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# console output formatting
print(f"Part 4: Conditionally Filter Lists of Loans\n")

# create an empty list for filtered inexpensive loans
inexpensive_loans = []

# BONUS: create an empty list for filtered expensive loans
expensive_loans = []

# set variable to provided loan threshold of $500
loan_threshold = 500

# loop through all dict entries in loans to filter into respective lists
for loan in loans:
    # if loan_price is less than or equal to loan_threshold
    if loan.get("loan_price") <= loan_threshold:
        # append the loan to the inexpensive loans list
        inexpensive_loans.append(loan)
    # BONUS: else if loan_price is greater than the loan_threshold
    elif loan.get("loan_price") > loan_threshold:
        # BONUS: append the loan to the expensive loans list
        expensive_loans.append(loan)

# BONUS: a function nicely formatting the list of loans to be printed to the console
def make_loan_list_message(list_of_loans):
    loan_list_message = ""
    for loan in list_of_loans:
        loan_list_message += str(loan) + "\n"    
    return loan_list_message

# BONUS: run the list of inexpensive loans through the function to generate nice output
list_of_inexpensive_loans = make_loan_list_message(inexpensive_loans)
# BONUS: run the list of expensive loans through the function to generate nice output
list_of_expensive_loans = make_loan_list_message(expensive_loans)

# print to console
print(f"List of inexpensive_loans:\n{list_of_inexpensive_loans}")

# BONUS: print to console
print(f"List of expensive_loans:\n{list_of_expensive_loans}")

# console output formatting
line_break(50)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# console output formatting
print(f"Part 5: Save the Results\n")

# create list of headers for csv
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# BONUS: create a function to write list values to csv
def write_to_csv(output_path, loan_list, header):
    # print in progress message to console
    print(f"{output_path}:\n\twriting to csv...")
    # invoke 'open()' within a 'with' statement to enable writing to a csv with whipped cream and a cherry on top
    with open(output_path, 'w', newline='') as csvfile:
        # establish the csvwriter pointing to the target
        csvwriter = csv.writer(csvfile)
        # write the header row to the csv
        csvwriter.writerow(header)
        # loop through each loan in the inexpensive loans list
        for loan in loan_list:
            # write the values of each loan to the csv
            csvwriter.writerow(loan.values())
    # print done message to console
    print(f"\tDONE.\n")

# assign name of inexpensive loans csv file to be written
output_path = Path("inexpensive_loans.csv")

# call the function to write inexpensive loans to csv
write_to_csv(output_path, inexpensive_loans, header)

# assign name of expensive loans csv file to be written
output_path = Path("expensive_loans.csv")

# call the function to write expensive loans to csv
write_to_csv(output_path, expensive_loans, header)

# console output formatting
line_break(50,'after')