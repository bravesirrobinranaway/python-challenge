#!/usr/bin/env python
# coding: utf-8

# In[74]:


#dependencies
import os
import csv
from collections import Counter


# In[75]:


#assign csv data to variable
election_results = open("Resources/election_data.csv", "r")


# In[76]:


#read csv
csv_reader = csv.reader(election_results, delimiter=",")


# In[77]:


#Read and print the header row
csv_header = next(csv_reader)
print(f"Header: {csv_header}")


# In[78]:


#Check to see if I can write the data to a new .csv file

with open("Resources/new_election_data.csv", "w", newline="") as new_file:
    csv_writer = csv.writer(new_file, delimiter=",")

    # Write the header row to the new file
    csv_writer.writerow(csv_header)

    # Write all data rows to the new file
    for row in csv_reader:
        csv_writer.writerow(row)


# In[79]:


# Reset the pointer of csv_reader
election_results.close()
election_results = open("Resources/election_data.csv", "r")
csv_reader = csv.reader(election_results, delimiter=",")
next(csv_reader)  # Skip the header row again

# Continue with more operations on csv_reader


# In[80]:


#assign the index to a variable
ballot_id_index = csv_header.index("Ballot ID")
candidate_index = csv_header.index("Candidate")

print(ballot_id_index)
print(candidate_index)


# In[81]:


#create variables to hold strings, lists, etc
ballot_id_column = []
candidate_column = []


# In[82]:


#populate lists with the data in a for loop

for row in csv_reader:
    ballot_id_column.append(row[ballot_id_index])
    candidate_column.append(row[candidate_index])
    

    


# In[83]:


#Assigns the number of ballots to a variable
ballot_count = len(ballot_id_column)
print(f"A total of {ballot_count} ballots were cast.")


# In[84]:


vote_count_dict = dict(Counter(candidate_column))
print(vote_count_dict)
vote_count_dict.keys()


# In[85]:


vote_total = len(candidate_column)
print(vote_total)


# In[86]:


vote_count_dict["Diana DeGette"]


# In[87]:


print(ballot_count)


# In[88]:


#identify the highest vote count
key = max(vote_count_dict, key=vote_count_dict.get)
winner = key
print(f"The winner is {winner}.")


# In[89]:


#iterate through the vote count dictionary to calculate 
#and store percentages

vote_percentage_dict = {}

for key, value in vote_count_dict.items():
    result = value / ballot_count
    result = "{:.0%}".format(result)
    vote_percentage_dict[key] = result

print(vote_percentage_dict)


# In[90]:


candidate_list = list(vote_percentage_dict)
print(candidate_list)


# In[91]:


print("Election Results")
print("----------------------------")
print(f"Total votes: {ballot_count}")
print("----------------------------")
print(f"{candidate_list[0]}: {vote_percentage_dict['Charles Casper Stockham']}  ({vote_count_dict['Charles Casper Stockham']})")
print(f"{candidate_list[1]}: {vote_percentage_dict['Diana DeGette']}  ({vote_count_dict['Diana DeGette']})")
print(f"{candidate_list[2]}: {vote_percentage_dict['Raymon Anthony Doane']}  ({vote_count_dict['Raymon Anthony Doane']})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


# In[96]:


#Export results to a text file

with open('Analysis_PyPoll/output_PyPoll.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("----------------------------\n")
    f.write(f"Total votes: {ballot_count}\n")
    f.write("----------------------------\n")
    f.write(f"{candidate_list[0]}: {vote_percentage_dict['Charles Casper Stockham']}  ({vote_count_dict['Charles Casper Stockham']})\n")
    f.write(f"{candidate_list[1]}: {vote_percentage_dict['Diana DeGette']}  ({vote_count_dict['Diana DeGette']})\n")
    f.write(f"{candidate_list[2]}: {vote_percentage_dict['Raymon Anthony Doane']}  ({vote_count_dict['Raymon Anthony Doane']})\n")
    f.write("----------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("----------------------------")
        


# In[ ]:





# In[ ]:





# In[95]:


print("The name of the output file is output_PyPoll.txt and it can be found in \nthe analysis_PyPoll folder for this program.")


# In[94]:


print("Thank you for running Hugh's jupyter_main_PyPoll.")


# In[ ]:


election_results.close()

