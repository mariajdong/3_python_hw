#import modules
import os
import csv

#define list variables: months, profit/loss, change in profits
months = []
profit_loss = []
change = []

#specify budget csv path
bankpath = os.path.join ("resources","budget_data.csv")

#read budget csv file
with open (bankpath) as bankfile:
    bankreader = csv.reader (bankfile, delimiter = ',')
    
    #specify header
    bankheader = next (bankreader)
    
    #begin loop through rows
    for row in bankreader:
        
        #add months, profit/loss, & change in profit to existing list
        months.append (row[0])
        #maintain integer status for calculations later
        profit_loss.append (int(row[1]))
    
    #begin loop through profit/loss list
    for x in range (len(profit_loss) - 1):
        
        #calculate change b/w each profit, add to list
        change.append (int(profit_loss[x + 1] - profit_loss[x]))

#calculate results
num_months = len (months)
net_profit = sum (profit_loss)
avg_change = sum (change) / len (change)
max_change = max (change)
min_change = min (change)

#calculate month indices to use w/ month list;
#'+1' is to find the month after the change has occurred.
max_month_index = (change.index(max_change) + 1)
min_month_index = (change.index(min_change) + 1)

max_month = months[max_month_index]
min_month = months[min_month_index]

#round average change to correct number of decimal places
avg_change_dec = round (avg_change, 2)

#define financial analysis string
financial_analysis = (f"""financial analysis
------------------------------
total: ${net_profit}
average change: ${avg_change_dec}
greatest increase in profits: {max_month} (${max_change})
greatest decrease in profits: {min_month} (${min_change})
""")

#print to terminal
print (financial_analysis)

#export analysis to .txt file
analysis_output = "analysis/analysis_output.txt"

#write analysis contents to .txt file
with open (analysis_output, 'w') as text:
    text.write (financial_analysis)