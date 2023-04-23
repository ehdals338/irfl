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