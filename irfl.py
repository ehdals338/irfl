from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import argparse

def irfl(bug_report, source_dir):
    """
    1.  Collect all documents (i.e., the bug report and all source files)
    2.  Compute tf-idf vectors of each document
    3.  Compute cosine similarity between each vector
    4.  Rank source files using the similarity
    5.  Report the top five files
    """
    # step 1: collect documents
    docs = [bug_report] # start with the path to the bug report
    for root, subgdirs, files in os.walk(source_dir): # recursively visit all subdirectory
        for f in files: #iterate over all files in each subdirectory
            if os.path.splitext(f)[1] == ".java": # if the file is a java source code (i.e., ".java")
                docs.append(os.path.join(root, f))
    #print(docs)

    # step 2: compute tf-idf vectors for everythin in docs
    vectorizer = TfidfVectorizer(input="filename", decode_error="ignore", stop_words="english") #filename들에 대하여 모르는게 있느면 ignore하고 english에 대한거는 stop
    tfidfs = vectorizer.fit_transform(docs)
    #print(tfidfs[0]) # 다 하면 엄청 많이 나올듯

    # step 3: compute cosine similarity between tfidf vectors
    sims = cosine_similarity(tfidfs)

    # step 4: get the document which is the most similar to bug_report
    # sims[0][1:] #행 인덱스 0, similarity between bug report and all other source files
    scores = sorted(zip(docs[1:], sims[0][1:]), reverse=True, key=lambda x: x[1])

    # stept 5: report the top 5
    for file, similarity in scores[:5]:
        print("{} ({})".format(file, similarity))

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IR Based Fault Localisation')
    parser.add_argument("-b", "--bug_report", required=True,
                        help='the text file that contains the bug report')
    parser.add_argument('-d', "--source_directory", required=True,
                        help='the root of the source directory')

    args = parser.parse_args()
    bug_report = args.bug_report
    source_dir = args.source_directory
    
    irfl(bug_report, source_dir)