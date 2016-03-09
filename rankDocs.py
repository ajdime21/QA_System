import math
from textblob import TextBlob as tb

#computes the term frequency (number of times a word appears in a document 'blob')
def tf(word,blob):
	return float(blob.words.count(word))/len(blob.words)
	
#returns the number of documents containing a word	
def contains(word,bloblist):
	return float(sum(1 for blob in bloblist if word in blob))

#computes inverse document frequency (measures how common a word is in all documents in bloblist
#common word means lower idf
def idf(word, bloblist):
	return float(math.log(len(bloblist)/(1+contains(word,bloblist))))

#computes the tf-idf score (i.e. tf*idf; high weight if high term freq in a doc and low doc freq of the term in the whole corpus
def tfidf(word,blob,bloblist):
	return float(tf(word,blob)*idf(word,bloblist))

def scoreDoc(keywordList, doc, doclist):
	sums=0
	for keyword in keywordList:
		sums=sums+tfidf(keyword,doc,doclist)
	return sums


def rankSentences(keywordList, doclist):
	scores={}
	docList=[tb(doc[1].decode('utf-8')) for doc in doclistEntries]
	keywordIDFs={}
	
	for w in keywordList:
		keywordIDFs[w]=idf(w, docList)
	
	for i in enumerate(doclist):
		text=tb(doc[1].decode('utf-8'))
		sums=0
		for w in keywordList:
			sums=sums+(tf(w,text)*keywordIDFs[w])
		scores=[doc[0]]={'score':sums,'object': Sentence}
	
	bestMatches=sorted(scores.items(),key=lambda x: x[1]['score'],reverse=True)
	return bestMatches[:0]
