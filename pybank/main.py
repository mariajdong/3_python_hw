#import modules
import os
import csv

#define list variables: months, profit/loss
months = []
profit_loss = []

#specify budget csv path
bankpath = os.path.join ("resources","budget_data.csv")

#read budget csv file
with open (bankpath) as bankfile:
    bankreader = csv.reader (bankfile,delimiter = ',')
    
    #specify header
    bankheader = next(bankreader)
    
    #begin loop through rows
    for row in bankreader:
        
        #add months & profit/loss to existing list
        months.append (row[0])
        #maintain integer status for calculations later
        profit_loss.append (int(row[1]))

