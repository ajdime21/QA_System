import sys
import json, simplejson
#import urllib2
from textblob import TextBlob as tb
#from nltk import PorterStemmer
from textblob import Word
import logging
from nltk.corpus import stopwords

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_queries():
	if len(sys.argv) > 1:
		queries = str(sys.argv[1:])
	else:
		f = open('query_list.txt','r')
		queries = []
		for row in f:
			queries.append(row.replace('\n',''))
		f.close()
	return queries

query_stems = []
#keywords are numbers, adjectives, nouns, and verbs... https://cs.nyu.edu/grishman/jet/guide/PennPOS.html	
keyword_POS=['CD','JJ','JJR','JJS','NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ',]

#takes in a query as a string and returns keywords
def parseQuery(queries):
	for q in queries:
		q = tb(q)
		qtags=q.tags
		query_wtags=[w[0].encode('utf-8') for w in qtags if w[1] in keyword_POS]
		#q_stemmed=[(PorterStemmer().stem_word(w[0].encode('utf-8')),w[1]) for w in qtags]
		query_stems.append(query_stems)
	return query_wtags

def main():
	queries = get_queries()
	queries = parseQuery(queries)
	logging.debug(queries)

if __name__ == "__main__":
	main()
