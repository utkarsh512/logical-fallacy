# Structure-aware BERT v4.0

For logical fallacy detection, we use auxiliary sentences, created from
dependency paths, paired with original text to perform sentence-pair
classification task on BERT.

## Which dependency paths to use

In this version, for a given text, we order the dependency path in *decreasing
order of their TF-IDF score*. Dependency paths are used in that order.

## How auxiliary embeddings are created

The auxiliary embeddings are created using `node2vec` algorithm. We use the
*Simple* approach to get dependency paths, convert these paths into a vector,
concatenate it with CLS token and use it for classification.