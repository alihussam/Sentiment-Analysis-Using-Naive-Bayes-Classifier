import re, csv, os, sys


path_of_file_to_clean = sys.argv[1]
path_of_clean_file_to_save = sys.argv[2]

file = open(str(path_of_file_to_clean),'r+')
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
    newsentence = newsentence.replace(';','')
    newsentence = newsentence.replace('!','')
    newsentence = newsentence.replace('-','')
    newsentence = newsentence.replace('/','')
    newsentence = newsentence.replace('(','')
    newsentence = newsentence.replace(')','')
    sentiments.append(tuple[1])
    sentence_list_final.append(newsentence)
    

    
field_names = ['Sentence', 'Sentiment']    
output_csv = open(str(path_of_clean_file_to_save),'a')
csv_writer = csv.DictWriter(output_csv, lineterminator='\n',  fieldnames=field_names)

for index in range(0,len(sentence_list_final)-1):
    csv_writer.writerow({"Sentence":sentence_list_final[index],
                     "Sentiment":sentiments[index]})

output_csv.close()
print("Test Data Created")
