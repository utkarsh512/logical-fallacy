# Structure-aware BERT v1.0

For logical fallacy detection, we use auxiliary sentences, created from
dependency paths, paired with original text to perform sentence-pair
classification task on BERT.

## Which dependency paths to use

In this version, for a given text, we order the dependency path in *decreasing
order of their frequency*. Dependency paths are used in that order.

## How auxiliary sentences are created

There are two approaches here:

### Verbose

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
you is nominal subject of oppose and proposal is direct object of oppose and 
extend is clausal modifier of noun (adjectival clause) of proposal and care is 
direct object of extend.
```

### Masked Verbose

```
Input text
----------
you oppose a senator's proposal to extend government-funded health 
care to poor minority children because that senator is a liberal democrat.

Dependency paths
----------------
[Grammar level] ('dobj', 'acl', 'dobj', 'nsubj')
[Word level]    ('care', 'extend', 'proposal', 'oppose', 'you'),

Masked input text
-----------------
[MASK_0] [MASK_1] a senator 's [MASK_2] to [MASK_3] government - funded health 
[MASK_4] to poor minority children because that senator is a liberal democrat .


Auxiliary sentence
------------------
[MASK_0] is nominal subject of [MASK_1] and [MASK_2] is direct object of 
[MASK_1] and [MASK_3] is clausal modifier of noun (adjectival clause) of 
[MASK_2] and [MASK_4] is direct object of [MASK_3].
```