import os
import csv

#path to folder
election_data = os.path.join('Resources', 'election_data.csv')

#open and read the file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csvhead = next(csvreader)

    #lists & variables to store data
    candidates = {}
    votes = []
    votespercand = 0
    total_votes = 0
    percent_votes = 0
    most_votes = 0

    #loop through data to get all candidates & votes
    for row in csvreader: 

        candidate = row[2]
        #add votes to list and add to vote count
        votes.append(total_votes)
        total_votes +=1

        #separate out candidates - add one each time the candidate appears
        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] = 1

#count number of votes for each candidate
for candidate in candidates:       

    #to determine winner, if has most votes...
    if candidates[candidate] > most_votes:
        most_votes = candidates[candidate]
        winner = candidate         

#print results to terminal
print('Election Results')
print('-'*30)
print('Total Votes: ' + str(total_votes))
print('-'*30)

#calculate % of votes for each candidate - only way I can get it to print correctly
for candidate in candidates:
    percent_votes = (candidates[candidate])/total_votes *100
    percent_votes = "{}% ".format(round(percent_votes, 3))
    print(f'{candidate}: {percent_votes} ({candidates[candidate]})') 

print('-'*30)
print('Winner: ' + str(winner))
print('-'*30)

#write to txt file
#set location for output
outputplace = os.path.join('Analysis', 'Election_Results.txt')

    # #open file to write
with open(outputplace, 'w', newline ='') as datafile:
    txtwriter = csv.writer(datafile, delimiter= ' ')

    #write to the file
    txtwriter.writerow(['Election Results'])
    txtwriter.writerow(['-'*30])
    txtwriter.writerow(['Total Votes:', total_votes])
    txtwriter.writerow(['-'*30])

    #to print % correctly
    for candidate in candidates:
        percent_votes = (candidates[candidate])/total_votes *100
        percent_votes = "{}% ".format(round(percent_votes, 3))
        txtwriter.writerow([f'{candidate}: {percent_votes} ({candidates[candidate]})'])
        
    txtwriter.writerow(['-'*30])
    txtwriter.writerow(['Winner: ', winner])
    txtwriter.writerow(['-'*30])