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

#Actual Naive Bayes Logic
def NaiveBayes(review, class_word_dict, closs_prob, class_review_count):
    prediction = 1.0
    sentence_words = Counter(re.split("\s+",review))
    for word in sentence_words:
        # print('---')
        #Adding one so that prediction dont become 0 by multiplying
        denom = sum(class_word_dict.values())+class_review_count
        # print(denom)
        prediction *= sentence_words.get(word) * ((class_word_dict.get(word, 0)+1) / float(denom))
    return prediction * closs_prob


#This function only run nive bayes for each sentence 
def Predict(test_data, result_file, negative_words, positive_words, negative_probab, positive_probab, no_negative_sentences, no_positive_sentences):
    field_names=["Sentence", "Sentiment Predicted","Positive Prob","Negative Prob"]
    classifications = []
    #Prepare write to write csv
    output_file_write = csv.DictWriter(result_file, lineterminator='\n', fieldnames=field_names)
    #Write first row for file
    output_file_write.writerow({"Sentence":"Review","Sentiment Predicted":"Sentiment",
    "Positive Prob":"Positive Prob", "Negative Prob":"Negative Prob"})    
    for sentence in test_data:
        neg_prob = NaiveBayes(sentence[0],negative_words,negative_probab,no_negative_sentences)
        pos_prob = NaiveBayes(sentence[0],positive_words,positive_probab,no_positive_sentences)
        if(neg_prob > pos_prob):
            output_file_write.writerow({"Sentence":sentence[0],"Sentiment Predicted":0,
            "Positive Prob":pos_prob, "Negative Prob":neg_prob})    
            classifications.append(0)
        else:
            output_file_write.writerow({"Sentence":sentence[0],"Sentiment Predicted":1,
            "Positive Prob":pos_prob, "Negative Prob":neg_prob})    
            classifications.append(1)
    return classifications

def CheckAccuracy(predicted_list,Original_labels):
  Correct=0
  for i in range(0,len(Original_labels)-1):
    if (str(predicted_list[i])==Original_labels[i][1]):
      Correct=Correct+1
  print('Model Accuracy: ',float(Correct)/len(Original_labels))




#Opening all files
train_file = open('Dataset/Processed_Data/train_data.csv', 'r')
test_file = open('Dataset/Processed_Data/test_data.csv', 'r')
result_file = open('results.csv', 'w+')

#Extracting data from train file
## This two lines return list of tuples [review, sentiment]
train_data = list(csv.reader(train_file))
test_data = list(csv.reader(test_file))

#These two lines calculate number of total sentences
total_sentence_train = len(train_data)
# print(total_sentence_test, total_sentence_train)

#Seperating data into two classes negative and positive
## Return -ve and +ve along with their counts
negative_text, no_negative_sentences = getText(train_data, '0')
positive_text, no_positive_sentences = getText(train_data, '1')
# print(negative_text, no_negative_sentences)

# \s+ = split when one or more space
## The function return key value pairs
## This gives unique -ve and +ve words along with count
negative_words = Counter(re.split('\s+', negative_text))
positive_words = Counter(re.split('\s+', positive_text))
# print(negative_words); print(positive_words);

# Now we calculate probabilites of both -ve and poitive words in train data
negative_probab = no_positive_sentences / float(total_sentence_train)
positive_probab = no_negative_sentences / float(total_sentence_train)
# print(negative_probab, positive_probab)

#Lets now predict with test data
predictions = Predict(test_data, result_file, negative_words, positive_words, negative_probab, positive_probab, no_negative_sentences, no_positive_sentences)

#Check Accuracy
CheckAccuracy(predictions, test_data)

#Close All Files
train_file.close()
test_file.close()
result_file.close()

