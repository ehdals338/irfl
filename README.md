## Information Retrieval (IR) Based Fault Localisation

We will use tf-idf Vector Space Modelling (VSM) of documents to measure the similarity between the bug report and all source code files. For the hands-on, we will skip the various pre-processing stages, and only use English natural language stopwords filtering. 

For the tf-idf vectorisation, we will use the `TfidfVectorizer` from the `sklearn` package (`sklearn.feature_extraction.text.TfidfVectorizer`). The API documentation is [here](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html). Note that you can submit a list of filenames to the vectorizer.

Given a matrix (i.e., a vector of vectors), you can use the pairwise `cosine_similarity` function from `sklearn` (`sklearn.metrics.pairwise.cosine_similarity`), whose documentation is [here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).