# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 16:30:44 2012

@author: dhanson
"""

from time import time
from sklearn.feature_extraction import text
from sklearn import decomposition
from Vectorizer import jsonLines

n_samples = 1000
n_features = 10000
n_topics = 10
n_top_words = 20

# Load the 20 newsgroups dataset and vectorize it using the most common word
# frequency with TF-IDF weighting (without top 5% stop words)

t0 = time()
print "Loading dataset and extracting TF-IDF features..."
#dataset = datasets.fetch_20newsgroups(shuffle=True, random_state=1)
dataset = jsonLines("datasets/1.json")
n_samples = len(dataset)
vectorizer = text.CountVectorizer(max_df=0.5, max_features=n_features, stop_words='english')
counts = vectorizer.fit_transform(dataset)
tfidf = text.TfidfTransformer().fit_transform(counts)


print "done in %0.3fs." % (time() - t0)

# Fit the NMF model
print "Fitting the NMF model on with n_samples=%d and n_features=%d..." % (
    n_samples, n_features)
nmf = decomposition.NMF(n_components=n_topics).fit(tfidf)
print "done in %0.3fs." % (time() - t0)

# Inverse the vectorizer vocabulary to be able
feature_names = vectorizer.get_feature_names()

for topic_idx, topic in enumerate(nmf.components_):
    print "Topic #%d:" % topic_idx
    print " ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]])
    print
    
results = nmf.transform(dataset)
    