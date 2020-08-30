# import the os module to join the file paths across operating systems
import os

# import Module for reading CSV files
import csv

budget_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Open CSV file
with open(budget_path) as budget_file:
	# read the CSV file
    budget_reader = csv.reader(budget_file, delimiter=',')


    # Calculate months included in the dataset


    # Calculate the net total amount of "Profit/Losses" over the entire period


    # Calculate the greatest increase in profits (date and amount) over the entire period


    # Calculate the greatest decrease in losses (date and amount) over the entire period
