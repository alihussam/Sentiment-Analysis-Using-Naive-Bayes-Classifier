import re, csv, os

#FIle exists: https://therenegadecoder.com/code/how-to-check-if-a-file-exists-in-python/
#re is RegEx module
#OPEN THE DATA FILE

#More details about open function https://stackabuse.com/file-handling-in-python/
file = open("Dataset/Raw_Data/yelp_labelled.txt",'r+')
data = file.read()
#print(data)

#Three list to store processed data
sentence_list = []
sentence_list_final = []
sentiments = []

# test = re.split('\n',data)
# print(test)

#re.split() args: pattern, string, maxsplit=0, flags=0
for sentence in re.split('\n',data):
#     print(sentence)
    sentence_list.append(sentence)

    
for index in range(0,len(sentence_list)-1):
    #print(sentence)
    tuple = re.split('\t',sentence_list[index])
    #Cleaning out possible punctuation marks
    newsentence = tuple[0].replace('.','')
    newsentence = newsentence.replace(',','')
    newsentence = newsentence.replace('!','')
    newsentence = newsentence.replace('-','')
    newsentence = newsentence.replace('/','')
    newsentence = newsentence.replace('(','')
    newsentence = newsentence.replace(')','')
    sentiments.append(tuple[1])
    sentence_list_final.append(newsentence)
    

    
field_names = ['Sentence', 'Sentiment']    
output_csv = open('Dataset/Processed_Data/train_data.csv','a')
csv_writer = csv.DictWriter(output_csv, lineterminator='\n',  fieldnames=field_names)

for index in range(0,len(sentence_list_final)-1):
    csv_writer.writerow({"Sentence":sentence_list_final[index],
                     "Sentiment":sentiments[index]})

output_csv.close()
print("Test Data Created")
