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
    greatest_increase = 0
    greatest_decrease = 0
    previous_row = ["",0]

    for row in budget_reader:
	    # Calculate months included in the dataset
	    if row[0] != "Date":
	    	total_months = total_months + 1

	    if row[1] != "Profit/Losses":
		    # Calculate the net total amount of "Profit/Losses" over the entire period
	    	total_profit_loss = total_profit_loss + int(row[1])


	    	monthly_increase_decrease = int(row[1]) - int(previous_row[1])
	    	# Test printing data
	    	print(f"Monthly increase/decrease: {row[0]} {monthly_increase_decrease}")

			# Calculate the greatest increase in profits (date and amount) over the entire period
			# The code below isn't the right calculation
	    	if greatest_increase < monthly_increase_decrease:
        	    greatest_increase = monthly_increase_decrease
        	    greatest_increase_month = str(row[0])

    		# Calculate the greatest decrease in losses (date and amount) over the entire period

	    	# Save previous row so we can make comparison in the next iteration
	    	previous_row = row

    # Calculate the average changes in Profit/Losses over the entire period
    # This calculation isn't what I'm supposed to do
    average_profit_loss = total_profit_loss / total_months

    # Print data to screen

    # Print total months
    print(f"Total Months: {total_months}")

    # Print total profit/loss
    print(f"Total: ${total_profit_loss}")

    # Print average changes
    print(f"Average Change: ${average_profit_loss}")

    # Print greatest increase in profits
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")

    # Print data to text file

