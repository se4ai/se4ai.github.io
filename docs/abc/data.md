---
layout: abc
title: About Data
---


## Summary

- Data can be _stuctured_ or _unstructured_;
- _Tables_ are one way to structure data. Tables have  _columns_ (also called  _features_ or _attributes_ or _variables_);
+ The columns may be _numeric_ (has numbers) or _symbolic_ (contain symbols).
- Features can be _independent_ or _dependnet_
- Dependent features (also called _goals_)  can be _classes_ or _objectives_

## About Data

Lets start at the very beginning-- its a very good place to start.
When we read we begin with a-b-c. When we mine we begin with... data.

## Unstructured Data

Reader beware: Most data does not arrive in a well-structured form (like that discussed below).
For example, when mining text we have to handle
spelling mistakes,
tables in inconstist formats,  the same words taking on different meanings, etc etc.
In fact, in text mining, it is not even clear where one cencept ends  and another begins.
For those reasons, text mining is so much fun.

In any case, when  data does not come in an unstructured form (and it usually does not) it is the task of the data scientist
to uncover that strucutre. This book has sevearl chapters on exactly that
process (see [data collection](/dm/collect), [data cleaning](/dm/clear),
[data labelling](dm/label) and [feature engineering](/dm/feature)).
For now, we'll assume some magician has waved a magic wand over the data to produce stuctured data.

## Structured Data

Different kinds of data miners work best of different kinds
of data. For structured data, that  data may be views as _tables_ of examples:

+ Tables have _columns_, also know as features or attributes or variables.
+ The columns may be _numeric_ (has numbers) or _symbolic_ (contain symbols).
+ Columns may contain missing values.
+ Tables have one _column_ per feature and one _row_ per example. 
+ Also, some columns are goals (things we want to predict using the
  other columns).
    - Goals are often called _dependent_ variables and the other columns ar called _independent_.
    -  Data mining algorithms seek combinations of the independent
       values that predict for the dependent values. 
    - Optimizing algirthms seek changes to the independent values
      that predict for _changes_ in the dependent values.

Many data miners learn models of the form

$$
y = f(x)
$$

where $x$ are the indepedent variabes and $y$ are the depedennt variables.

Optimiers, on the other hand
learn models the explore changes (deltas) to variables:

$$
{\Delta}y = f'({\Delta}x)
$$

In the above $ f' $ is some function learned from $f$ that shows us how changes in the independent variables effects the dependent ones.
When all the data is numeric and conforms to a simple distribution, then simple mathematic tools are enough to learn $ f' $.

For example, in _text mining_, where there is one column per
word and one row per document, the columns contain many missing values
(since not all words appear in all documents) and there may be
hundreds of thousands of columns.

Text mining applications can have many columns. _Big Data_
applications can have any number of columns and millions to billions
of rows.  For such large large data sets, a complete analysis may be
impossible.  Hence, these must be sampled probabilistically using
algorithms like [PageRank](/glossary#Pagerank) or [Naive Bayes](#Pagerank).
  
On the other hand, when there are very few rows, data mining may fail
since there are too few examples to support summarization. For such
spare tables, _k-th nearest neighbors_ ([kNN](/glossary#KNN)) may be best. kNN makes
conclusions about new examples by looking at their neighborhood in the
space of old examples. Hence, kNN only needs a few (or even only one)
similar examples to make conclusions.

If a table has many goals, then some may be competing; e.g. it may not
be possible to find a car with the twin goals of low cost and low
miles per gallon.  Such competing multi-goal problems can be studied
using a _multi-objective optimizer_ like the genetic algorithms used
in [NSGA-II](/glossary#Nsgaii).

If a table has no goal columns, then this is an _unsupervised_
learning problem that might be addressed by (say) finding clusters of
similar rows using, say, [K-means](/glossary#Kmeans) or [EM](/glossary#Em).  An alternate approach, taken
by the [APRORI](/glossary#apriori)  association rule learner, is to assume that ever column
is a goal and to look for what combinations of any values predict for
any combination of any other.

If a table has one goal, the this is a _supervised_ learning problem
where the task is to find combinations of values from the other
columns that predict for the goal values.

+ Note that for data sets with one discrete goal feature,
  it is common to call that goal the _class_ of the data set.
  
The following table shows a _simple data mining_ problem. Such problems
are characterized by tables with just a
few columns and not many rows (say, dozens to thousands). Traditionally,
such simple data mining problems have been explored by [C4.5](#C45) and 
[CART](/glossary#Cart)
(and note that with some clever sampling of the data, it is
possible to scale these traditional learners to Big Data problems.  

In this table, we are trying to predict for the goal of
`play?` (and note that `temp` and `humidity` are numeric columns and
there are no missing values).

 outlook |   temp |  humidity |  windy |   play?
-------- |   ---- |  -------- |  ----- |  -----
overcast |     64 |        65 |   TRUE |    yes
overcast |     72 |        90 |   TRUE |    yes
overcast |     81 |        75 |  FALSE |    yes
overcast |     83 |        86 |  FALSE |    yes
rainy    |     65 |        70 |   TRUE |     no
rainy    |     71 |        91 |   TRUE |     no
rainy    |     68 |        80 |  FALSE |    yes
rainy    |     70 |        96 |  FALSE |    yes
rainy    |     75 |        80 |  FALSE |    yes
sunny    |     69 |        70 |  FALSE |    yes
sunny    |     72 |        95 |  FALSE |     no
sunny    |     75 |        70 |   TRUE |    yes
sunny    |     80 |        90 |   TRUE |     no
sunny    |     85 |        85 |  FALSE |     no



