import sys
import json, simplejson
import urllib2
from textblob import TextBlob as tb
from nltk import PorterStemmer
from textblob import Word
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_queries():
	if len(sys.argv) > 1:
		queries = str(sys.argv[1:])
	else:
		f = open('query_list.txt','rU')
		queries = []
		for row in f:
			queries.append(row.replace('\n',''))
		f.close()
	return queries

#takes in a query as a string and returns keywords
def parseQuery(queries):
	query_stems = []
	for q in queries:
		q = tb(q)
		qtags=q.tags
		q_stemmed=[w[0].encode('utf-8') for w in qtags]
		q_stemmed=[(PorterStemmer().stem_word(w[0].encode('utf-8')),w[1]) for w in qtags]
		query_stems.append(q_stemmed)
	return query_stems

def main():
	queries = get_queries()
	queries = parseQuery(queries)
	logging.debug(queries)

if __name__ == "__main__":
	main()