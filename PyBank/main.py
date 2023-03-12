import pandas as pd

df = pd.read_csv("Resources/budget_data.csv")

# The total number of months included in the dataset
total_months = len(df)

# The net total amount of "Profit/Losses" over the entire period
net_total = df["Profit/Losses"].sum()

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = df["Profit/Losses"].diff()
average_change = changes.mean()

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = changes.max()
greatest_increase_date = df.loc[changes.idxmax(), "Date"]

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = changes.min()
greatest_decrease_date = df.loc[changes.idxmin(), "Date"]

# Analysis
results = []
results.append("Financial Analysis")
results.append("----------------------------")
results.append(f"Total Months: {total_months}")
results.append(f"Total: ${net_total}")
results.append(f"Average Change: ${average_change:.2f}")
results.append(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.0f})")
results.append(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.0f})")

# Write results to a text file
with open("output.txt", "w") as file:
    file.write('\n'.join(results))