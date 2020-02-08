import os
import csv


def avgchange(avglist=[]) :  
    global Avg_change
    global Month_max_change
    global Month_min_change
    global Maxval
    global Minval
    enum_list =[]
    changelist =[]
    # create a list of just the profit/loss column
    for row in list_comp:
        to_nbr=float (row[1])
        enum_list.append(to_nbr)
    
    TotalChange=0
    chgTracker=0
    for x in range(0,len(enum_list)-1):
        n1=int(enum_list[x])
        n2=int(enum_list[x+1])

        # Find the change and append to the change list
        n3 =n2 - n1
        changelist.append(n3)
        chgTracker +=1

        #cal the total change
        TotalChange +=n3
        x =x+1

    #Cal avg change
    Avg_change=TotalChange/chgTracker

    # find max change value and date
    Maxval =int( max(changelist))
    maxindex =changelist.index(Maxval)
    Month_max_change= list_comp[maxindex+1][0]

    # find min change value and date
    Minval = int(min(changelist))
    minindex =changelist.index(Minval)
    Month_min_change= list_comp[minindex+1][0]

    #return Avg_change,Minval,Maxval


file_path = os.path.join("..","Python-challenge","budget_data.csv")

with open(file_path,newline="") as budget_data_csvfile:

    budget_data_csvreader = csv.reader(budget_data_csvfile, delimiter=",")

    # Total and number of months
    for row in budget_data_csvreader:
        list_comp = [row for row in budget_data_csvreader]
        
        nbr_months = len(list_comp)#list length

        Total =0
        counter = 0
        for row in list_comp:
            counter += 1
            nextrow =int(row[1])
            Total += nextrow

avgchange(list_comp)
        
print("     Financial Analysis")
print("     --------------------------")
print("     Total Months: "+str(nbr_months))
print("     Total: $"+str(Total))
print("     Average Change: "+str(round(Avg_change,2)))
print(f"     Greatest Increase in Profits: {Month_max_change} (${str(Maxval)})")
print(f"     Greatest Decrease in Profits: {Month_min_change} (${str(Minval)})")





            


    


