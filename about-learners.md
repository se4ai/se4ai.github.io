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

The goal of this chapter is to offer certain core intuitions, common features,
about learners. It is not a comprehensive guide (for that, see [the excellent Ian Witten book]
on data mining](REFS#witten-2016)
 but it does introduce much of the learning technology used
later in this book.

----

<<<<<<< HEAD
## Columns and Rows

=======
>>>>>>> 04dbb69eaea898aa0af810898f6b706b44a57b8c
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

<<<<<<< HEAD
A set of rows is sometimes called a table, or a relation. In such sets, we
often keep statistics on each column. 
If `n,s` are instances of class `Num,Sym` then `n+x, s+x`
are methods that add `x` to the summary. For example

```python
n = Num()
for x in [1,2,3,4]: n+x
print(n, n.sd)

---
title: " ==> {'n': 4, 'mu': 2.5, 'lo': 1, 'hi': 4}"
layout: default
---
---
title: " ==> sd = 1.29"
layout: default
---

#-----------
s = Sym()
for x in 'abbcccc': s+x
print(s,s.mode, s.ent)

==> Sym{bag={'a': 1, 'b': 2, 'c': 4}, n=7} c 1.38
==> mode = 'c'
==> ent = 1.38
```
In the `Num`eric summaries, we see counts of how many `n` numbers seen, their minimum and maximum values (denoted `lo,hi`), 
and their standard deviation `sd` which is a measure of the diversity of a set of numbers.
The standard deviation of  a set of $$n$$ numbers is
$$\sigma(Y,n) = \sqrt\frac{\sum_i (Y_i-Y')^2}{n-1}$$ where $$Y'$$ is the mean value for $Y$. Standard deviation is minimal (zero)
when all the numbers are the same.

In the `Sym`bolic summary, we see counts of how many `n` numbers were seen, their most common value (denoted`mode`),
and their entropy `ent` (which is a measure of the diversity of a set of symbols.
The entropy of $n$ symbols occuring at frequency $$f_1,f_2,..$$ etc
is $$=\sum_i p_i\log_2p_i$$ where $$p_i=f_i/n$$.
Entropy  is minimal (zero)
when all the symbols  are the same.

=======
>>>>>>> 04dbb69eaea898aa0af810898f6b706b44a57b8c
Supervised learners learn a model $$f$$ of the form $$Y=f(X)$$.
Unsupervised learners ignore the dependent variable
and group together  similar rows, based on their $$X$$ values.
For that grouping, some distance function is required. A
standard distance function between rows $$a,b$$ with $$f$$ 
features

$$
\mathcal{dist}(a,b,f,r,p=2) = \left(\frac{1}{\sqrt{|f|}}\right)\left(\sum_{i\in f} \mathcal{diff}(r,i,a_i,b_i)^p\right)^{1/p}
$$

where:

- $$r$$ is the set of all rows;
- $$f$$ are the features we are considering  (usually the independent variables[^trick1])
<<<<<<< HEAD
- $$p=2$$ makes this the Euclidean distance (but it is worthy exploring other values); 
=======
- $$p=2$$ makes this the Euclidean distance; 
>>>>>>> 04dbb69eaea898aa0af810898f6b706b44a57b8c
- dividing by the root of the number of features makes this range from 0 to 1

[^trick1]: Sometimes $f$ can be the dependent variables. In two-tiered
clustering you might cluster first by the dependent variables, and
then by the independent variables.  Since the number of dependents
is typically much less than the independents, this can run very
fast.

<<<<<<< HEAD
In the _dist_ equation, the _diff_ function for symbolic and numberic columns. For numbers, a usual _diff_ has the range $$0..1$$ and
is calulated as follows:

$$\mathcal{diff}(r,i,a_i,b_i) = (r.col[i].norm(a_i) = r.col[i].b_i)^p$$

where $$r.col.norm(x)$$ is a function that normalises $$x$$ to the range $$0..1$$ using $$\frac{x-lo}{hi - lo + 0.0000001}$$
(i.e. using the smallest and largest value seen in column $$i$$) and                                          $$0.0000001$$
is a small constant added to the denominator to avoid divide-by-zero errors. 

For symbols, a usual $$diff$$ is 

$$\mathcal{diff}(r,i,a_i,b_i) = 0\; \mathcal{if}\;a_i==b_i\;\mathcall{else} 1$$

If either of $$a_i,b_i$$ are unknown values then _diff_ returns the maximal possible difference. 

- For symbols, that maximum value is 1
- For numbers, if one value $x$ is known then it is normalized to $x'$ and the distance is set to the maximum possible value; i.e.

$$ (1-x')\; \mathcal{if}\; x'> 0.5\; \mathcal{else}\; x'$$

- And, for numbers if both values are unknwon, then _diff_ returns 1.
 
### Clustering (Unsupervised Learning)

The simplest (and sometimes slowest) learner is a clusterer.
Clustering ignores any class or goal variables and group together similar rows using some distance function.
Clustering can be slow since, if implemented naively, it requires multiple $$O(N^2)$$ comparison between all rows.
The famous K-means algorithm reduces that to $$O(kN)$$ as follows:

1. Declare that  $$K$$ rows (picked at random) are the _centroids_;
2. Marks each example with the id of its nearest centroid;
3. Finds the central point of all the rows marked with the same centroid.
4. Declares those new central points to be the new centroids
5. Goto 1

K-means terminates when the next set of centroids are similar to the last ones. There are several heuristics for determinging a good value for $$k$$:

- One way is to always us $$k=$$; i.e. recursively apply $$k=$$ k-means to divide the data into 2, then 4, then 8.. clusters (stopping when you hit, say, $$\sqrt{N}$$ of the original data set size;
- Another way is the _elbow_ test. 
    - Define some measure of "goodness" for a cluster (e.g. median distance of members to the centroid). 
    - Increase $$k$$ [looking for the "knee" in the curve](https://bl.ocks.org/rpgove/0060ff3b656618e9136b) after which more $$k$$ does not produce "good clusters" (e.g. those with lower distance members to the centroid)
    - Use the $$k$$ at the "knee".

Once you know your $$k$$, you've got to select $$k$$ centroids
One way is to do it randomly (see the mini-batch k-means algorithm shown below), 
Another way is to use k-means++, which always tries to select centroids that are far away from the existing centroids:


- For $$z$$ in 1 to $$k$$ do
    - Pick any row $$r_0$$ and make  set $$\mathit{center[z] = r_0$$.
    - For every other row, $$r_i$$ (a) find the nearest center made so far; (b) find the distance $$d_i$$ between $$r_i$$ and that center
    - Pick $$r_i$$ as the  next center at probability $$d_i^2$$  [^pick]

[^picl]: to pick $$x_i\in X$$ at probability  $$p_i$$,  find  $$P=\sum p_i$$.  Sort $$x_i \in X$$ in descending order by $$p_i$$.
Pick a random number $$0\le r \le 1$$ and run over sorted $X$. At each step, set $$r=r-  p_i/P$$. When $$r \le 0$$, return $$x_i$$.

It is insightful to think of K-means as an example of _expectiation minimization_ algorithms.
Such algorithms make guesses, then change something to minimize the errors associated with those gusess (in this case, move the centroids).

[Mini-batch K-means](REFS#sculley-2015) is a more memory efficient  version of K-means.
This variant never loads all the examples into main memory. Instead, it only loads _batches_ of rows of size  $$B$$. 
The first $$k$$ rows (picked at raond) become the first $$k$$ centroids. Rows arrive after that (in the same batch) add themselves to a cluster assocated with the nearest
centroid. When the batch is done, each cluster adjust its centroids by reflecting over each row in the centroid:

- For the first row, the centroid moves itself half way towards the row; 
- For the second row, the centroid moves itself one-third of the way  towards the row; 
- And so on such that for the nth row, the centroid moves itself $$1/(n+1)$$th  the way  towards the row; 

The next batch of $$B$$ rows is read and the process repeats. Note that for this to work, we must have a way of moving some cluster $$c$$ towards
row $$r$$. When processing the $$z$$-th item in a cluster:

- For numeric column $$i$$, $$c_i = (1 - 1/z)*c_i + 1/z*r_i$$
- For symbolic columns, at probablity $$1/z$$, $$c_i = r_i$$

An even more effecient clustering algorithm uses random projections. The above clustering algorithms 
are very sensitive to quirks in the distance function. One way to mitigate for those quirks
is sort out the rows using multiple, randomly generated distance measures. Sure, a few may be less-than-perfect
but the more often a random project says two rows are similar, then the more likely they are actually are similar.

Here is the RP0 random projection clustering (there are many others, but this one is pretty simple):

1. Let $$M,P=32,10$$ (say)
2. Read the data. While  you have less  than $2M$ rows, add the rows into a local data cache.
3. If you have more than  $2M$$ rows, then divide:
    - $$P$$ times; pick any two _poles_ (the rows $$x,y$$) in the batch and find the distance between them.
    - Pick the pair of poles with maximum distance.
    - Divide the according to whether or not they are closer to one pole or the other.
    - For each division, goto 2

Note that RP0 is like a faster version of the recursive $$k=2$$-means algorithm described above.

There are many  interesting ways to modify  RP0:
- Do not sub-cluster all data. E.g. only divide on (say) X=50% of data selected (a) at random or (b) spread out between the poles.
This way ensures that sub-trees get smaller and smaller.
- Ignore (some) newly arrived data. In this aproach,   an _anomaly detector_ could report if the newly
arriving data is anything like what has been seend before (if so, we can ignore it since it does not add anything
to the model). For example,  in step2, as new data arrives, its distance could be compared to (say) $M$ other things already in the cluster.
If that is less than the $$Y$$ times the median value of all the distances previously seen in the cluster, the new example is boring and might be ignored
(For this approach, [Fayola Peters](REFS#peters-2015) suggests $Y=1$).
In step2, once $$M$$ examples have been read  a classifier/regression algorithm could be executed on the examples in that cluster and executed on any newly arriving examples.

## From Unsupervised to Supervised Learning

Clustering is a knowledge acquisition technique. In short, rather than asking everyone about everything, first cluster the data
then only check a sample of rows from each cluster.

For example, clustering is one way to help _active learning_.
Often we have more rows than labels (a.k.a. classes) for that data (that is, most of our data is suitable only for unsupervised learning). This is a common situation.
For example:

- Suppose it takes 15 seconds to read a four line Github issue before you can say if that issue is 
  "about a bug" or "otherwise".
- Suppose further you have 10,000 such issues to read. Assume you can stand doing that for 20 hours in a standard 35 hour work week (which is actually a  bit of a stretch), and suppose that
  you label issues ina  group of two (so that when labels disagree, you go ask the other person). That labelling task will take two people, four weeks to complete[^mt]-- and you many just
  not have time for that.

[^mt]: Some might comment that this four weeks could be done in an hour, via
[crowdsourcing](https://www.youtube.com/watch?v=Pjm1uYbuyk4),  That's true BUT consider- when comissioning a crowdsourcing rig, you have to first certify the efficacy of that rig. That means
you need some "ground truth" to check the conclusions. So now you are back to labelling some significant percentage of the data. 

For another example:

- Suppose you are doing effort estimation for software projects. It is relatively much harder to access financial details about a project (e.g. the salaries of the workers) than
  the product details about that software.
- This means that your data has many independent rows (the product details) but little or no dependent information.


Given some oracle that can label data (e.g. a human being), and assuming that oracle takes time $$t$$ or costs $$x$$  everytime you ask it a question,
then _active learning_ is the process of learning an adequate model after asking the oracle using minimum time and/or cost.

(Aside: Another way to handle label-shortage is  _semi-supervised_ learning that finds things similar to the labelled examples,
then propagates the labels to the unlabelled space. For example, if you cluster data, then (a) each cluster will have a few labels and (b) the unlabelled
examples in each cluster can be given that cluster's majority label.  Of course, you still have to check if the resulting new labels are correct.
If you want to do that check effeciently (i.e. not check everything) then you'll need some smart way to check a sub-sample of the new labels.
At which point you are back to active learning-- but perhaps with fewer overall queries to the oracle).

An _aquisition function_ is one way to guide an active learner:

- Given a model built from the $$L$$ labels seen to date, go forth and make guesses; i.e. use the tiny model built so far to guess labels for the remaining data.
- Apply the aqusition function to select the most interesting guess
     - e.g. select the guess with the highest/lowest score (if you are truing to maximimze/ minimize something).
     - e.g. select the guess with the highest uncertainty
     - e.g. or select the guess with higest score plus uncertainty
- Give that most interesting guess  to an oracle. Ask them to label it
- Build a new model from  the $$L+1$$ labels.

Here are some important details about the above process:

- When building a new model using the new label, it is useful if the new model can be incrementally 
    - If the number of labelled examples is very small, then anything will do. 
    - But as the labelled space grows, consider using learners that incrementally update very quickly (e.g. fast nearest-neighbors; Naive Bayes).
- The uncertainty of a guess can be determines in different ways, depending on the learner:
    - Within [NaiveBayes](img/boundary.png), the most uncertain guess is the one that with nearly equal probabilities of being in multiple classes. 
    - Within [Logistic regression](https://en.wikipedia.org/wiki/Logistic_regression#/media/File:Exam_pass_logistic_curve.jpeg), the most uncertain guess is the one closest to 0.5.
    - Within [Support Vector Machines](https://quantdare.com/wp-content/uploads/2016/09/svm2.png), the most uncertain row is the one that falls mid-way between the support vectors
    - In an [ensemble learning](https://miro.medium.com/max/590/1*DUaQoSKHX09hLG0QcGApTg.png), an uncertain guess is the one made by the smallest majoirity. For example consider an ensemble of
      built from (say) ten 90% samples of the current data. That ensemble offers a label when 6,7,8,9 or 10 ensemble members vote the same way.
      In that case, the most uncertain guess would be from a majoroty of only 6.
    - [Gaussian process models](https://miro.medium.com/max/700/1*PF8XTtgVm1UYTuRc3U2ePQ.jpeg) offer a mean and standard deviation for each prediction.


## Supervised Learning

desciretiaon is slicing and dividing columns

learning is slicing and dividing rows
clusters- does not use class var
naive bayes
decision trees
logisitic regression
support vector machines (a favorite in text minig)
ensele learning
guesiann process models

Fast supervised learning


Dont traing on  examples , use some sunset (selected at random, or selected froma  cluserr)
move the elarning into the clsuterr so  icnremetnaly do top-down recrsive clsutering and build one mdoel per elaf clsuter)

FYI- currently exepreimentaing with a upwards growth clsuterr called BUBBLES that has the _bellwether_ premise; i.e.
that there exist a small number of examples that can be used to reason about the rest. In essence, _bellwether_
is an _instance selection_ algorithm that uses some target learner as the instance selection tool. If the data
set is large, BUBBLES
is useful sice it reduces the number of examples passed to the learner:

- BUBBLES recrusively clusters the data.
- Each node hold data $$D$$ which is recursively clustered into $$M$$ child clusters.
- One model is learned from the data in each leaf and pushed to its parents.
- At each internal node
    - $$M$$ models are received from its children.
    - Each model $$M_1$$ is tested on the $$M-1$$ sub-clusters that were not used to generate it. 
    - The $$\mathcal{best}$$ models are the  $$(M_1,M_2,M_3..)\subseteq M$$ of models with indistinguishably best performance,
    - A new model $$M_0$$ is build from $D_0$$, a random sample of size $$|D|/|M|$$ of the data in $$(D_1,D_2,D_3..)$$. 
    - $$M_0$$ is tested on  $$D-D0$$.
    - The new $$\mathcal{best'}$$ model is either $$M_0$$ (if it outperforms $$\mathcal{best}$$) or any one of $$\mathcal{best}$$.
    - If there is no parent  node, BUBBLES returns $$\mathcal{best'}$$.
    - Else if pushes $$\mathcal{best'}$$ to the aprent.


maths methods highly optimized. For example, SVM with a lienar kernel runs very fast over a large text corpus. 

XXX active:
 and suppose there are

Divide the data,a t random, into 10 buckets.
   - Build one model  rows have class/goal values:
   - Also, when  humans are checking the class columns:
   - Within each cluster, ten times, select 90\% of the data. Find the oddest item (the o

g. Since the learner chooses the examples, the number of examples to learn a concept can often be much lower than the number required in normal supervised learning. 

Of all the above algorithms, standard K-means might produce the best clusters (since it is always reasoning over all the data). On the other hand,
the other variants might scale to larger data sets. 

There any many other ways to cluster data. For a more complete survey, see any textbook on data mining or [some of the excellent on-line tutorials](https://scikit-learn.org/stable/modules/clustering.html).


- range cuts, column cutts (feature selection)
contrast sets (avoding dullr egions)

### naive bayes group and the class and loomfor dfferente ebween theing
XXX decision trees cut on the class
cover and differentiate make a decision the spin hthru the rest

## Divide nums (discreitzation)


## Quiz

---
title: " u dont nroamlize what happens?"
layout: default
---
---
title: " given standard deviation forumla, derive sd"
layout: default
---
---
title: " given entropy  forumla, derive e"
layout: default
---
---
title: " distance between two rows"
layout: default
---
---
title: " derive the cosine rule"
layout: default
---
=======
 or independent 
In the latter case, we also have 
   <X,Y>

wererun over data of the form


The simplest (and sometimes slowest) learner is a cluster.
Clsuters ignore any class or goal variables
>>>>>>> 04dbb69eaea898aa0af810898f6b706b44a57b8c
