import csv
import re
from collections import Counter


#This function takes data and the sentiment of which the text is to 
# be sperated
def getText(data, sentiment):
    extracted = ''
    count = 0
    #test_list = []
    for row in data:
        if row[1] == sentiment:
            extracted += row[0]+ ' '
            #test_list.append(row[0])
            count += 1
    return extracted, count

#This functions return the no# of labels in data
def getLabelCount(data, sentiment):
    count = 0
    for row in data:
        if row[1] == sentiment:
            count += 1
    return count







#Opening all files
train_file = open('Dataset/Processed_Data/train_data.csv', 'r')
#result_file = open('results.csv', 'w+')

#Extracting data from train file
train_data = list(csv.reader(train_file))
total_sentence = len(train_data)

#Seperating data into two classes
negative_text, no_negative_sentences = getText(train_data, '0')
positive_text, no_positive_sentences = getText(train_data, '1')


#\s+ = split when one or more space
negative_words = Counter(re.split('\s+', negative_text))
positive_words = Counter(re.split('\s+', positive_text))

train_file.close()
#result_file.close()

