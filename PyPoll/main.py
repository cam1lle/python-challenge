import pandas as pd 

df = pd.read_csv("Resources/election_data.csv")

#The total number of votes cast
total_votes = len(df)

#A complete list of candidates who received votes
candidate_list = df["Candidate"].unique().tolist()

#The percentage of votes each candidate won
vote_counts = df["Candidate"].value_counts(normalize=True) * 100

#The total number of votes each candidate won
total_votes_per_candidate = df["Candidate"].value_counts()

#The winner of the election based on popular vote
winner = total_votes_per_candidate.idxmax()

# Analysis
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate in candidate_list:
    results.append(f"{candidate}: {vote_counts[candidate]:.3f}% ({total_votes_per_candidate[candidate]})")
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print and export the results
output_file = "output.txt"
with open(output_file, "w") as file:
    for result in results:
        print(result)
        file.write(result + "\n")
print(f"Results exported to {output_file}")