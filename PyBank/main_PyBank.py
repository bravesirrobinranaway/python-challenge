#!/usr/bin/env python
# coding: utf-8

# In[256]:


#dependencies
import os
import csv
from collections import Counter
from datetime import datetime


# In[257]:


#defines an averaging function
def Average(lst):
    return sum(lst) / len(lst)


# In[258]:


#assign csv data to variable
budget_data_csv = open("Resources/budget_data.csv", "r")


# In[259]:


#read csv
csv_reader = csv.reader(budget_data_csv, delimiter=",")


# In[260]:


#Read and print the header row
csv_header = next(csv_reader)
print(f"Header: {csv_header}")


# In[261]:


#Read and print all rows of csv data 
#(this was a quality check)
#for row in budget_data_csv:
    #print(row)


# In[262]:


#assign the index to a variable
date_index = csv_header.index("Date")
profit_losses_index = csv_header.index("Profit/Losses")


# In[263]:


#create a list to store the date data  
#create a variable & starting value for total & previous profit/loss
#create list to store the monthly changes

dates = []
total = 0
prev_profit_loss = 0
monthly_changes = []


# In[264]:


#populate the list with all of the dates in the csv file
for row in csv_reader:
    dates.append(row[date_index])
    total = total + float(row[profit_losses_index])
    if prev_profit_loss == 0:
        prev_profit_loss = float(row[profit_losses_index])
    else:
        monthly_change = float(row[profit_losses_index]) - prev_profit_loss
        monthly_changes.append(monthly_change)
        prev_profit_loss = float(row[profit_losses_index]) 


# In[265]:


#quality check
print(dates)


# In[266]:


# Use the len function to generate the frequency count
month_counts = len(dates)


# In[267]:


# Print the frequency count of months
print(month_counts)


# In[268]:


print(total)


# In[269]:


print(monthly_changes)


# In[270]:


average_change = round((Average(monthly_changes)), 2)
print(average_change)


# In[271]:


greatest_increase = max(monthly_changes)
print(greatest_increase)


# In[272]:


greatest_decrease = min(monthly_changes)
print(greatest_decrease)


# In[273]:


print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_counts}")
print(f"Total profit/loss: ${total}")
print(f"Average change: ${average_change}")
print(f"Greatest increase in profits: ${greatest_increase}")
print(f"Greatest decrease in profits: ${greatest_decrease}")


# In[275]:


#Export results to a text file

with open('Analysis_PyBank/output_PyBank.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total months: {month_counts}\n")
    f.write(f"Total profit/loss: ${total}\n")
    f.write(f"Average change: ${average_change}\n")
    f.write(f"Greatest increase in profits: ${greatest_increase}\n")
    f.write(f"Greatest decrease in profits: ${greatest_decrease}\n")
        


# In[280]:


print("The name of the output file is output_PyBank.txt and it can be found in \nthe analysis_PyBank folder for this program.")


# In[281]:


print("Thank you for running Hugh's jupyter_main_PyBank.\nUp next, PyPoll!")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


test_list = [40, 30, 20, 10, 0, 90, 80, 70, 60, -20, 50]
print(min(test_list))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


budget_data_csv.close()

