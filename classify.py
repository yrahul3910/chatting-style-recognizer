import pandas as pd
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

content = []
data = []
common = []


def remove_non_ascii(text):
	return ''.join([i if ord(i) < 128 else ' ' for i in text])


def remove_words(array):
	final = []
	words = []
	for line in array:
		words = line.split()
		for x in common:
			if x in words:
				words.remove(x)
		# unneeded words removed, join them
		new_line = ' '.join(words)
		final.append(new_line)
	return final


# 1.txt is where the first person's chat history is put
# and used to train the algorithm
with open("1.txt", encoding="utf8") as f:
	content = f.readlines()
# common is a list of 100 most common English words
with open("common") as f:
	common = f.readlines()
# Remove non-ASCII and common words from input
content = [w.replace("\n", '') for w in content]
content = [remove_non_ascii(w) for w in content]
content = remove_words(content)
for i in content:
	data.append([i, "Person1"]) # First create 2D arrays
# Same thing with second person
with open("2.txt", encoding="utf8") as f:
	content = f.readlines()
content = [w.replace("\n", '') for w in content]
content = [remove_non_ascii(w) for w in content]
content = remove_words(content)
for i in content:
	data.append([i, "Person2"])
# Third person
with open("3.txt", encoding="utf8") as f:
	content = f.readlines()
content = [w.replace("\n", '') for w in content]
content = [remove_non_ascii(w) for w in content]
content = remove_words(content)
for i in content:
	data.append([i, "Person3"])
# You could add more people here

data = [[remove_non_ascii(item) for item in row] for row in data]
# We have data in the 2D array. Now we gotta convert to numpy array

data_frame = pd.DataFrame(data, columns=list('xy'))
# Shuffle data for randomness
data_frame = data_frame.reindex(numpy.random.permutation(data_frame.index))
# Create feautre vectors
count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(data_frame['x'].values)

# Create a Multinomial Naive Bayes classifier with Laplace smoothing
# alpha parameter is 1 by default so it uses Laplace smoothing
classifier = MultinomialNB()
targets = data_frame['y'].values
classifier.fit(counts, targets)

success = 0
fail = 0
sample = [] # Put the test data in sample array
# Below file contains test data for first person
# You can substitute test data for any person
with open("test_P1.txt", encoding="utf8") as f:
	sample = f.readlines()
sample = [w.replace("\n", '') for w in sample]
sample = [remove_non_ascii(w) for w in sample]
sample = remove_words(sample)

sample_count = count_vectorizer.transform(sample)
predictions = classifier.predict(sample_count)
for i in predictions:
	if i == "Person1":
		success += 1
	else:
		fail += 1
print("Success="+str(success)+"\nFail="+str(fail))
print("Success%="+str(success*100/(fail+success))[0:5])