import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

tMonths = []
tProfit_Losses = []
Changes = []
Average_Change = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    for row in csvreader:
        tMonths.append(row[0])
        tProfit_Losses.append(int(row[1]))

#Caluculate total number of months included in the dataset
Total_Months = len(tMonths)

#Caluculate the net total amount of "Profit/Losses" over the entire period
Profit_Losses = sum(tProfit_Losses)

#Caluculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
for i in range(1, Total_Months):
    change = tProfit_Losses[i] - tProfit_Losses[i-1]
    Changes.append(change)
Average_Change = sum(Changes) / len(Changes)

#Caluculate the Greatest Increase in profits (date and amount) over the entire period
Greatest_Increase = max(Changes)
Greatest_Increase_Date = tMonths[Changes.index(Greatest_Increase) + 1]


#Caluculate the Greatest Decrease in profits (date and amount) over the entire period
Greatest_Decrease = min(Changes)
Greatest_Decrease_Date = tMonths[Changes.index(Greatest_Decrease) - 1]

print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total Net Profit/Losses: ${Profit_Losses}")
print(f"Average Change: ${Average_Change: .2f}")
print(f"Greatest Profit Increase : {Greatest_Increase_Date} (${Greatest_Increase})")
print(f"Greatest Profit Decrease : {Greatest_Decrease_Date} (${Greatest_Decrease})")

