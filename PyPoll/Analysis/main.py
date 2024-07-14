import os
import csv

election_data_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    Totalcst_Votes = list(csvreader)
    Total_Votes = len(Totalcst_Votes)

    print("Election Results")
    print("--------------------")

    print(f"Total Votes: {Total_Votes}")
    print(f"-------------------")

    Candidates = {}
    for row in Totalcst_Votes:
        if row [2] not in Candidates:
            Candidates[row[2]] = 1
        else:
            Candidates[row[2]] += 1

    for candidate, Totalcst_Votes in Candidates.items():
        percentage = (Totalcst_Votes / Total_Votes) * 100

        print(f'{candidate}: {percentage:.3f}% ({Totalcst_Votes})')

        winner = max(Candidates, key=Candidates.get)

    print(f"--------------------")
    print(f'Winner: {winner}')

#C:\Users\lord1\PythonCode\python-challenge\PyPoll\Resources