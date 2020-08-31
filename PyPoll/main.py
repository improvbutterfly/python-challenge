# Program to read CSV with "voter ID," "county" and "candidate" data, analyse results, and output to screen and text file
# Authored by Dominica Corless

# import the os module to join the file paths across operating systems
import os

# import Module for reading CSV files
import csv

election_path = os.path.join('.', 'Resources', 'election_data.csv')

# Path for output text file
election_results = os.path.join('.', 'analysis', 'election_results.txt')

# Create a dictionary to store the votes for each candidate
candidates = {}

#Open CSV file
with open(election_path) as election_file:
	# read the CSV file
	election_reader = csv.reader(election_file, delimiter=',')

	#Initialize variables
	total_votes = 0

	for row in election_reader:
		voter_ID = row[0]
		county = row[1]
		candidate = row[2]

		if voter_ID != "Voter ID":
			total_votes = total_votes + 1

			# Check if candidate already exists in dictionary
			if candidate in candidates:
				# Add a new vote
				votes = candidates[candidate] + 1

				# Update key
				update_candidate = {candidate: votes}
				candidates.update(update_candidate)
			# If candidate does not exist in dictionary, add them
			else:
				candidates.update({candidate: 1})

# Open file to write results
write_file = open(election_results, 'w')

# Print election results to screen and text file
print("Election Results")
print("----------------------------")

write_file.write(f"Election Results\n")
write_file.write(f"----------------------------\n")

# Print total votes
print(f"Total Votes: {total_votes}")
print("----------------------------")

write_file.write(f"Total Votes: {total_votes}\n")
write_file.write(f"----------------------------\n")

# Initialize comparison vote counter
most_votes = 0

# Print data from candidate dictionary
for candidate, votes in candidates.items():
	# Calculate percentage of vote
	vote_percentage = "{:.3f}".format(votes / total_votes * 100)

	# Determine if candidate has more votes than previous candidate
	if votes > most_votes:
		most_votes = votes
		winner = candidate

	# Print candidate data to screen
	print(f"{candidate}: {vote_percentage}% ({votes})")

	# Print candidate data to text file
	write_file.write(f"{candidate}: {vote_percentage}% ({votes})\n")

# Print winner to screen
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Print winner to text file
write_file.write(f"----------------------------\n")
write_file.write(f"Winner: {winner}\n")
write_file.write(f"----------------------------\n")

# Close text file
write_file.close()
