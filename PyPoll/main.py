import os
import csv

#lists/variables to hold info
months_tot = []
profits_losses = []
change_pl = []
avg_change = 0
previous_month = 0
greatestinc = 0
greatestdec = 0

#path to folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#open and read the file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csvhead = next(csvreader)
    
   #loop through all data & put info into the lists
    for row in csvreader:
        months_tot.append(row[0])
        profits_losses.append(int(row[1]))
  
        #calculate changes from month to month 
        avg_change +=1

        if (avg_change > 1):
            change_pl.append(float(row[1]) - previous_month)
        previous_month = float(row[1])

    #calculate total months
    allmonths = len(months_tot)
    
    totalPL = sum(profits_losses)
    totalPL = '${}'.format(totalPL)

    #calculate average change
    average_chg = (sum(change_pl) / len(change_pl))
    average_chg = '${:,.2f}'.format(average_chg)

    #find greatest profit
    greatest_inc = max(change_pl)
    inc_month = months_tot[change_pl.index(greatest_inc) + 1 ]
    greatest_inc = '${}'.format(greatest_inc)
    
    #find greatest decrease
    greatest_dec = min(change_pl)
    dec_month = months_tot[change_pl.index(greatest_dec) +1 ]
    greatest_dec = '${}'.format(greatest_dec)
    

    #print results to terminal
    print('Financial Analysis')
    print('-'*30)
    print(f'Total Months:', allmonths)
    print(f'Total:', totalPL)
    print(f'Average Change:', average_chg)
    print(f'Greatest Increase in Profits:', (inc_month + " " + "(" + greatest_inc + ")"))
    print(f'Greatest Decrease in Profits:', (dec_month + " " + "(" + greatest_dec + ")"))
    
#combine print statements to print in txt file
output = ('Financial Analysis' + '\n' +'-'*30 + '\n' + 'Total Months: ' + str(allmonths) + '\n' + 'Total: ' + totalPL + '\n' 'Average Change: ' + average_chg + '\n' + 'Greatest Increase in Profits:' + (inc_month + " " + "(" + greatest_inc + ")") + '\n' + 'Greatest Decrease in Profits:' + (dec_month + " " + "(" + greatest_dec + ")"))

#write to txt file
with open('Analysis/Financial_analysis.txt', 'w') as tf:
    tf.write(output)
