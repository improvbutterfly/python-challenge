# import the os module to join the file paths across operating systems
import os

# import Module for reading CSV files
import csv

budget_path = os.path.join('.', 'Resources', 'budget_data.csv')

#Open CSV file
with open(budget_path) as budget_file:
	# read the CSV file
    budget_reader = csv.reader(budget_file, delimiter=',')

    # Set initial variables to 0
    total_months = 0
    total_profit_loss = 0

    for row in budget_reader:
	    # Calculate months included in the dataset
	    if row[0] != "Date":
	    	total_months = total_months + 1

	    # Calculate the net total amount of "Profit/Losses" over the entire period
	    if row[1] != "Profit/Losses":
	    	total_profit_loss = total_profit_loss + int(row[1])

	    # Calculate the greatest increase in profits (date and amount) over the entire period


    	# Calculate the greatest decrease in losses (date and amount) over the entire period


    # Print data to screen

    # Test total_months data
    print(f"Total months: {total_months}")

    # Print total profit/loss
    print(f"Total profit/loss: {total_profit_loss}")
    # Print data to text file

