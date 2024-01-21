## Information Retrieval (IR) Based Fault Localisation

We will use tf-idf Vector Space Modelling (VSM) of documents to measure the similarity between the bug report and all source code files. For the hands-on, we will skip the various pre-processing stages, and only use English natural language stopwords filtering. 

### Dependencies

We will use [scikit-learn](https://scikit-learn.org/stable/) to implement the vectorization and the similarity measurement.

### Instructions

The provided `irfl.py` file has a skeleton to implement the IRFL heuristic. For the tf-idf vectorisation, we will use the `TfidfVectorizer` from the `sklearn` package (`sklearn.feature_extraction.text.TfidfVectorizer`). The API documentation is [here](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). Note that you can submit a list of filenames to the vectorizer. This is why the step 1 is to collect all filenames. Step 2 is to use TfidfVectorizer to get the vector representations.

1.  Collect all documents (i.e., the bug report and all source files): 
2.  Compute tf-idf vectors of each document

Given a matrix (i.e., a vector of vectors), you can use the pairwise `cosine_similarity` function from `sklearn` (`sklearn.metrics.pairwise.cosine_similarity`), whose documentation is [here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).

3.  Compute cosine similarity between each vector
4.  Rank source files using the similarity
5.  Report the top five files

