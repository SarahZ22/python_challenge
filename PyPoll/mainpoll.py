#code created with help of teacher, study group, office hours and tutor
#dependencies
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

#write to txt file (trying different way)
with open('Analysis/Election_Results.txt', 'w') as tf:
    tf.write('Election Results')
    tf.write('\n')
    tf.write('-'*30)
    tf.write('\n')
    tf.write('Total Votes: ' + str(total_votes))
    tf.write('\n')
    tf.write('-'*30)
    tf.write('\n')
    #to print % correctly
    for candidate in candidates:
        percent_votes = (candidates[candidate])/total_votes *100
        percent_votes = "{}% ".format(round(percent_votes, 3))
        tf.write(f'{candidate}: {percent_votes} ({candidates[candidate]})')
        tf.write('\n')
    tf.write('-'*30)
    tf.write('\n')
    tf.write('Winner: ' + str(winner))
    tf.write('\n')
    tf.write('-'*30)