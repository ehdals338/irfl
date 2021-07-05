from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os
import argparse

def irfl(bug_report, source_dir):
    """
    -- Collect all documents (i.e., the bug report and all source files)
    -- Compute tf-idf vectors of each document
    -- Compute cosine similarity between each vector
    -- Rank source files using the similarity
    -- Report the top five
    """
    
    for similarity, filename in ranking[:5]:
        print(f"{filename} --- cosine similarity {similarity}")

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