import os
import csv

file_path = os.path.join("..","Python-Challenge","budget_data.csv")

with open(file_path,newline="") as budget_data_csvfile:

    budget_data_csvreader = csv.reader(budget_data_csvfile, delimiter=",")

    for row in budget_data_csvreader:
        list_comp = [row for row[0] in budget_data_csvreader]
        nbr_months = len(list_comp)
        print(len(list_comp))