# Structure-aware BERT v2.0

For logical fallacy detection, we use auxiliary sentences, created from
dependency paths, paired with original text to perform sentence-pair
classification task on BERT.

## Which dependency paths to use

In this version, for a given text, we order the dependency path in *decreasing
order of their frequency*. Dependency paths are used in that order.

## How auxiliary sentences are created

The auxiliary sentences are created as

```
Input text
----------
you oppose a senator's proposal to extend government-funded health 
care to poor minority children because that senator is a liberal democrat.

Dependency paths
----------------
[Grammar level] ('dobj', 'acl', 'dobj', 'nsubj')
[Word level]    ('care', 'extend', 'proposal', 'oppose', 'you'),

Auxiliary sentence
------------------
direct object leads to adjectival clause leads to direct object
leads to nominal subject 
```