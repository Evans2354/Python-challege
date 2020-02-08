import os
import csv


file_path = os.path.join("..","Python-challenge","budget_data.csv")

with open(file_path,newline="") as budget_data_csvfile:

    budget_data_csvreader = csv.reader(budget_data_csvfile, delimiter=",")

    for row in budget_data_csvreader:
        list_comp = [row for row in budget_data_csvreader]
        nbr_months = len(list_comp)
        Total =0
        counter = 0
        for row in list_comp:
            counter += 1
            nextrow =int(row[1])
            Total += nextrow
        print(Total)
    

def avgchange(avglist=[]) :    
    enum_list =[]
    changelist =[]
    # create a list of just the profit/loss column
    for row in list_comp:
        to_nbr=float (row[1])
        enum_list.append(to_nbr)
    
    # Find the change and append to the change list
    Minval =0.0
    Maxval =0.0
    TotalChange=0
    chgTracker=0
    for x in range(0,len(enum_list)-1):
        n1=int(enum_list[x])
        n2=int(enum_list[x+1])
        n3 =n2 - n1
        changelist.append(n3)
        chgTracker +=1
        TotalChange +=n3
        x =x+1

    Avg_change=TotalChange/chgTracker
    Maxval =float( max(changelist))
    Minval = float(min(changelist))
    print(Minval)
    print(Maxval)
    return Avg_change, Minval ,Maxval
print(avgchange(list_comp))




            


    


