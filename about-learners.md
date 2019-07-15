---
title: " About Learners"
layout: default
---

Learners divide old data  into (say):

- things that are similar or different (this is called
  clustering)
- things you care about 
- things you don't 
- things you want to avoid.

They then can look at new data to learn if
what kind of thing it is.


Optimizers change things. That is, once you have learned
that you like X and do not like Y, then an optimizer
could suggest "do X - Y". Optimizers are discussed later.

Learners process examples  (also called rows)
of the form
$$(X,Y)$$ were:

- $$X$$ are one or more independent variables (a.k.a. inputs)
- $$Y$$ are the dependent variables we want to achieve
  (a.k.a. outputs).

Note that variables are also called features, attributes,
or columns.
The outputs
can be:

- one  class that may be symbolic
  (e.g. defective=True or False) or numeric (e.g. development
  effort).
- one or more numeric goals that divide into things
  we love/hate that we want to minimize/maximize (respectively);
  e.g. amount of reused code or number of bugs.

Supervised learners learn a model $$f$$ of the form $$Y=f(X)$$.
Unsupervised learners ignore the dependent variable
and group together  similar rows, based on their $$X$$ values.
For that grouping, some distance function is required. A
standard distance function between rows $a,b$ with $i$ 
is:

$$
\mathcal{dist}(a,b,f,p=2) = \left(\frac{1}{\sqrt{|f|}}\right)\left(\sum_{i\in f} \mathcal{diff}(a_i,b_i)^p\right)^(1/p)
$$

where:

- $$f$$ are the features we are considering  (usually the independent variables[^trick1])
- $$p=2$$ makes this the Euclidean distance; 
- dividing by the root of the number of features makes this range from 0 to 1

[^trick1]: Sometimes $f$ can be the dependent variables. In two-tiered
clustering you might cluster first by the dependent variables, and
then by the independent variables.  Since the number of dependents
is typically much less than the independents, this can run very
fast.

 or independent 
In the latter case, we also have 
   <X,Y>

wererun over data of the form


The simplest (and sometimes slowest) learner is a cluster.
Clsuters ignore any class or goal variables
