---
title: " # Baseline for an "Adequate" AI"
layout: default
---


Software engineering is about engineering and engineering is about
generate a produce of adequate quality, given the available constraints.
What does that mean for AI-enhanced software?

Within AI toolkits
we find hundreds of classifiers, regression tools, neural nets, support
vector machines, evolutionary algorithms, ant-colony optimizers, etc etc, etc[^wskj].
These primitives can be combined in millions of ways, then tuned in quadrillions of ways  (see the very active research literature
on all these methods). 
So given a new problem, which learner/optimizer should we apply? 

[^wskj]:

This is a very hard problem. [Wolpert](REFS:wolpert-2013)
reports in his famous No Free Lunch
Theorems (NFL) that if some optimizer/learner works best for some data, then some
other optimizer/learner
will work best for other
data. 
NFL warns that when
new data arrives, you need _commissioning experiments_; i.e. try a variety of techniques before you can
find what words best for the local data.
For a small taste of that NFL proof, consider the following example (from Wikipedia).
Consider a tiny universe that exists for two days and on each day contains exactly one object
(a square or a triangle). The universe has four possible histories:

- (square, triangle): the universe contains a square on day 1, and a triangle on day 2
- (square, square)
- (triangle, triangle)
-  (triangle, square)

Any prediction strategy that succeeds for history #2, by predicting a square on day 2 if there is a square on day 1, will fail on history #1, and vice versa. If all histories are equally likely, then any prediction strategy will score the same, with the same accuracy rate of 0.5

In the worst case, NFL tells us that what works in the best may never work best in the future
and we are doomed to forever fumble between  poor choices for  optimizer/data miners.
Happily, recent work offers a somewhat more optimistic (and more operational)
results.
 It turns out that 
(when comparing optimizers and data miners),
the greater the performance gain desired,
<a href="http://www.cs.cmu.edu/~gmontane/pdfs/montanez-2013-bounding.pdf">
the fewer the learners  exist that produce
at least such a performance gain</a>.
See the <a href="https://arxiv.org/abs/1603.06560">Hyperband optimizer</a> for
an adaptive approach to pruning away less-than-great methods.
Also, for many learners/optimizers, their
performance is indistinguishable for anything less than some &epsilon; value.
So if we divide the output space into bins of width &epsilon;
means we can stop looking once we find a few methods that 
<a href="https://arxiv.org/pdf/1803.04608.pdf">falls into the best &epsilon; bins</a>.)</p>

When conducting such commissioning experiments, it is methodologically useful to have a _baseline method_; i.e. an algorithm which can generate floor performance values. Such baselines let a developer quickly rule out any method that falls “below the floor”. With this, researchers and industrial practitioners can achieve fast early results, while also gaining some guidance in all their subsequent experimentation (specifically: “try to beat the baseline”).

Using baselines for analyzing algorithms has been endorsed by several
experienced researchers:

- In his [textbook on empirical
methods for artificial intelligence](pdf/empiricalAI.pdf), Cohen
strongly recommends comparing supposedly sophisticated systems
against simpler alternatives. In the machine learning community,
- Holte  uses the [OneR baseline
algorithm](https://www.mlpack.org/papers/ds.pdf) 
as a scout that runs
ahead of a more complicated learners as a way to judge the complexity
of up-coming tasks. 
- In the software engineering community, Sarro et al  
et al.  recently proposed [baseline methods for effort
estimation](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.8862&rep=rep1&type=pdf).
- Shepperd and Macdonnel argue convincingly that 
measurements
are best viewed as [ratios compared to measurements taken from some
minimal baseline
system](https://bura.brunel.ac.uk/bitstream/2438/6473/4/IST_Invited_2011_v7.pdf). 
- Work on cross-versus within-company cost
estimation has also recommended the use of some [very simple
baseline](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.8862&rep=rep1&type=pdf)
- I've offered several good baseline AI tools for SE tasks. In both the
  following, my graduate students were able to replace widely used very complex
  solutions with much simple alternative. For example:
    - Search-based SE: [A Baseline Method For Search-Based Software Engineering](http://greggay.com/pdf/10baseline.pdf)
    - Data mining: [Bellwethers: A Baseline Method For Transfer Learning](https://arxiv.org/pdf/1703.06218)
    - Optimizing: ["Sampling"' as a Baseline Optimizer for Search-based Software Engineering](https://arxiv.org/pdf/1608.07617)



So for this subject, we propose replacing the question of "what AI tool is best"
with two other questions that make more sense to engineers racing to deliver
products with limited time and resources:

- How can we quickly commission an initial, adequate, AI baseline system?
- What can we do to test and improve on that baseline?


## But what is a "good" baseline?


Here's one list of what a "baseline" means. Items 1..10 are adapted
from [Sarro, TOSEM'18](http://www0.cs.ucl.ac.uk/staff/F.Sarro/resource/papers/SarroTOSEM18.pdf).
(which we extend with our own notes). The other items come from my experience. 

<small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> 
Note also that  the following list offers a road map for future research in SE+AI. Find
  cases where some of these points do not matter. Find ways to enhance
  existing systems such that they perform better on the following criteria.
  Etc.
</small>
The key thing to note about the following is that one system may not satisfy
all these criteria (in fact, no known system satisfied all of them). That said,
 each
of the following points is important. And by reflecting on the value of each
point
for a particular AI application, we naturally consider and review (and possibly
discard) important design alternatives.

<br clear=all>

### The Checklist

Now stay calm citizens of FSS'18. The following is not as complex as it looks. 
  while there are many complex ways to support the following, there
  are also very simple ways that can work very well for each. And for your project, you only
  have to understand a **one** of the following.
  

**1. SIMPLE:** Be simple to describe, implement, and interpret (i.e. interpret the output for business uses).

- My current "simplest" methods is [Fast-and-Frugal decision trees](https://arxiv.org/pdf/1803.05067.pdf) (or see also [here](http://library.mpib-berlin.mpg.de/ft/awk/AWK_Intuitive_2011.pdf));
  which is available in a nice
  [R-package](https://cran.r-project.org/web/packages/FFTrees/vignettes/guide.html).

**2. REASONABLE:** Offer comparable performance to standard methods.

- So note the great paradox of simplicity research
- <small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Curious fact: evaluation can get so hard that we usually  try to milk it for everything that can.
So "cross val" experiments lead us to [ensemble learning](http://menzies.us/pdf/11comba.pdf) then to [boosting](https://pdfs.semanticscholar.org/79ea/6a5a68e05065f82acd11a478aa7eac5f6c06.pdf);
"round robin" lead to [transfer learning](http://menzies.us/pdf/13transferEffort.pdf);
"jiggle a little" lead to [evolutionary methods](http://www0.cs.ucl.ac.uk/staff/M.Harman/ACM-surveys-sbse.pdf);
evolutionary methods.
</small>It is very hard to be simple
    - Cause the simplest thing has to be compared against other, more complex, things.


**3. STABLE:** Be <strike>deterministic</strike> stable in its outcomes


- I've replaced deterministic with stable, since I think that is more important.  
- Instability is very unsettling for software project managers struggling to find general policies. Project managers lose faith in the results of software analytics if those results keep changing. Also, such instability prevents project managers from offering clear guidelines on what to change, or what to avoid, in a project.
- And [instability plagues SE data](https://link.springer.com/article/10.1007/s10664-011-9193-5). For example:
     - [Here](http://menzies.us/pdf/12gense.pdf), 
          Fig1, are the coefficients learned by regression on 20
           67% samples of some training data. Note their WILD instability.
- One trick for increasing stability is not to focus on all the smaller details 
    - e.g.  when learning regression equations, do not use all the variables;
    - e.g. when learning rules, avoid wide conditions
    - e.g. when learning trees, do not learn deep trees).
- Of course, if you optimize for simplicity, you may pay a performance penalty.

**4a. INTUITIVE:** Be applicable to mixed qualitative and quantitative data.

- It is good to use numeric and symbolic data.
- It is useful to be able to initial a systems with qualitative intuitions.
     - Then, at least, you can compare the output to what folks already
          believe.
        - But be warned, in SE, the beliefs of many developers are...
                [dubious](http://web.cs.ucdavis.edu/~devanbu/belief+evidence.pdf).
        - If for no other reasons that humans have [numerous cognitive
          biases](http://images.mentalfloss.com/sites/default/files/styles/insert_main_wide_image/public/cognitive_biases.png)
               - For a really long list of those biases, see
                 [Wikipedia](https://en.wikipedia.org/wiki/List_of_cognitive_biases) or [this chart](https://en.wikipedia.org/wiki/List_of_cognitive_biases#/media/File:The_Cognitive_Bias_Codex_-_180%2B_biases,_designed_by_John_Manoogian_III_(jm3).png)
- It is useful to be able to guide model construction via high-level qualitative goals.
   -  One useful technology here are [Bayes nets](https://www.eecs.qmul.ac.uk/~norman/papers/fentonMMR_Full_v1_0.pdf) which can be either initially
      drawn by people, then revised by data miners, or vice versa.
   - Another trick is to use some incremental rule learning algorithm that updates
  many possible new rules, then scores them by their distance to old rules (and
  the best new rules are those that are closest to old and score highest). In
  that rig, user background beliefs would become the first generation rules.
   - Yet another method is to use multi-objective optimizers that fit rule
     learner to human biases.

**4b. COMPREHENSIBLE:**

This is connected to 4a.

- Essential for communities critiquing ideas. 
- If the only person reading a model is a carburetor, then we can expect little push back. But if your models are about policies that humans have to implement, then I take it as axiomatic that humans will want to read and critique the models.

**5. GENERAL:** Offer some explanatory information regarding the prediction
  by representing generalized properties of the underlying data.

- Many systems offer only "point" solutions; i.e. examples of what might be useful.
    - Given _N_ attributes, a point solution offers exact values for all attributes.
         - E.g. the output of most evolutionary programs
         - E.g. all instance-based (nearest neighbor) methods
    - E.g. A happy author might be editing this particular file and this particular time and place. 
- Some systems offer solutions that hold over a volume;
    - I.e. they ignore some values while saying things like _x > 10_ for
          others.
    - E.g. Happy authors might be editing html files on many computers
          (and when they do it does not matter).
- One way to generalize  a instance-based method is to cluster the solutions,
  then only report ranges that are different in different clusters.

**6. NO MAGIC:** Have no magic parameters within the modeling process that require tuning. 

- E.g. for random forests, engineers have to decide on how many trees are
      included in the forest.
- Alternatively, if such tunings exist, then the must be some [automatic method](https://arxiv.org/pdf/1705.03697.pdf) for selecting what
      tunings are best for particular data sets.

**7. AVAILABLE:** Be publicly available via a reference implementation and associated environment for execution.

- In this day and age of Docker images and package managers and Github-like
      environments where everyone can load up each other's
      code at the drop of a hat, it makes no sense for some baseline tool to be
      inaccessible.

**8. USEFUL:** Generally be more accurate than a random guess or (e.g. an estimate based purely on the distribution of the response variable).

- E.g. evaluate the output via "standardarized error"; i.e. compare the
  prediction to some some prediction generated from (say) the median value of the response variable.


**9. CHEAP:** Do not be expensive to apply.

- Here we mean that the CPU, Ram, and disk space required to make something
      work is not crazy high.
- "CHEAP is important since ~Reproducing and improving an old ideas means that you can reproduce that old result. Also, certifying that new ideas often means multiple runs over many sub-samples of the data. Such reproducibility and certification is impractical when such reproduction is impractically slow


**10. ROBUST:** I.e. does not change much over different data splits and validation
  methods?

- And if it does vary wildly, can it find ways to find regions in the data
      where the data conclusions are stable.

**11. GOAL-AWARE:**
Different goals means different models. AND multiple goals = no problem!

- This is important since most data miners build models that optimizer for a single goal (e.g. minimize error or least-square error) yet business users often want their data miners to achieve many goals.
- For example, if we want to ask "what to do" rather than "what is", then we
  need a planner, not a classifier. Of course, in that case, the classifier can
  be used as a what-if guide to assess different plans.

**12. CONTEXT-AWARE:** context-aware:

<small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Easy path context
awareness:  first cluster the data, then build different models
for different clusters: see [NbTrees](http://robotics.stanford.edu/~ronnyk/nbtree.pdf).
</small>

- Knows that local parts of data generate different models.
- E.g. hierarchically clusters the data and builds one model per cluster.
- While general principles are good, so too is how to handle particular contexts. For example, in general, exercise is good for maintaining healthy. However, in the particular context of patients who have just had cardiac surgery, then that general principle has to be carefully tailored to particular patients. ideas need to be updated.


**13. HUMBLE:**  
<small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Easy path to
certification envelopes: cluster data, report k items per cluster.
</small>


- Can publish succinct certification envelope that can report when new data is
  out-of-scope to what was seen before.(so we know when not to trust)
    - This is important since the delivered data mined models should be able to recognize when new data is out-of-scope of anything they’ve seen before. This means, at runtime, having access to the data used to build that model. 
    - Note that phrase succinct here: certification envelopes cannot include all the data relating to a model, otherwise every hard drive in the world will soon fill up.
- Another form of humility is knowing when the baseline should be replaced with
  something else. 
  Holte  uses the [OneR baseline
algorithm](https://www.mlpack.org/papers/ds.pdf) 
as a scout that runs
ahead of a more complicated learners as a way to judge the complexity
of up-coming tasks. 

**14. STREAMING:**

- Can run over an infinite stream of data, updating itself (or knows when to go
back to old versions of itself).
- <small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Easy path to
anomaly detection: cluster data, report items that fall far from each cluster.
</small>
Can detect anomalies (when new inputs differ from old training data).
This is the trigger for re-learning.

<br clear=all>
**15. SHARABLE:** Knows how to transfer models, data, between contexts.

<small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Easy path to
lightweight sharing: just share reduced data from context awareness.
</small>

- Need some way to keep the volume of shared data down (otherwise "sharing" would clog the Internet).
- Such transfer may requires some transformation of the source data to the target data.

<br clear=all>
** 16. PRIVACY-AWARE: **

<small class="sidenote">
<i class="fa  fa-hand-o-right fa-4x"></i> Easy path to
privacy: within the clusters of the certification envelope, just share k items per cluster, each slightly mutated.
See [LACE2](http://menzies.us/pdf/15lace2.pdf).
</small>

- Can hide an individual's data
- This is essential when sharing a certification envelope

<br clear=all>
## Project

The project of this class is to apply the above to AI tools applied to SE
problems. Even trying to apply the above
and not getting anywhere, would also be fine (just as you long as
you document your comprehension of the ideas of baselines,  along the way). 
So go seek, or build, good baselines:

- Take any SE problem and ask are
the current methods "baselines?". Would simpler alternatives suffice? 
- Can you make the method simpler to use; 
    - e.g. replace it with something much simpler to implement and explain
    - e.g. apply an optimizer to a data mining to find better settings from that
data miner? 
- If you replace the complex with the simpler, what (if any) is the performance penalty?
- Can you make the method use less RAM or be faster to use; 
    - e.g. see what happens if you learn on just X% of the data (randomly
      selected) for    
      X &isin; {50,25,10,5,1}%?
    - If you apply a prototype generator, can you select/build a very small 
      subset of the data from which learning is faster and just as effective?
          - Finding prototypes can be as easy as "cluster and take just a few
            from each cluster"
          - But there are [many other
            methods](https://www.researchgate.net/profile/Jose_Francisco_Martinez-Trinidad/publication/220637923_A_review_of_instance_selection_methods/links/0912f50c21a20bd92b000000.pdf)
    - eg. apply a data miner to an optimizer to divide up the data to make the
      whole process much faster?
See [500+ faster than deep learning](https://arxiv.org/pdf/1802.05319.pdf). 
- Does that method need additional support to enable explanation of their output?
- Do their models fail the stability test? 
    - How does that  method respond if you run it N times on 90% of the data? 
    - And if they do, can you find regions of the data where the performance is stable?
- How to reduce the CPU and RAM and runtime requirements
of that method by large amounts e.g. 
see [500+ faster than deep learning](https://arxiv.org/pdf/1802.05319.pdf). 
- If we stream over the data, how soon does this model stabilize? 
- If we inject mutations into the data, can
this method be used to recognize that strange data? Once the weird data
arrives, how long (if ever) before the model recovers? 
- If a model is update, can be it done some _minimally_; i.e. with least change to the existing model?
- etc
- etc
- etc

## All Connected

The more we compress the smaller the memory and the faster we learn and the less we need to share (so
more privacy).

The more we understand the data's prototypes the more we know what is usual/
unusual so we more we know what is anomalous so the easier it is to offer a
certification envelope

Note that if our compression method is somehow hierarchical and if we track the
errors seen by our learners in different subtrees then the more we know which
parts of the model need revising (and which can stay the same). Which means we
only make revisions to the parts that matter, leaving the rest stable.


## Other Requirements

### No eval tools 

Tests conclusion stability

- across multiple data sets (if
  available) 
- or across multiple subsets of know scenarios

See [Evaluation](eval) for many examples of that kind of evaluation.

- Note that these can significantly increase the computational cost of using learners. 
- Hence, the need to [faster](faster), [lighter](lighter) AI algorithms. 

## No support for stats tests

- Check if _this_ treatment has
   same effect as _that_ treatment.
- Need at least two tests: 
         [significance](../gloss/significance)  and [effect size](../gloss/effectsize)
- I also think you need a third test;
    - Something
       that clusters the treatments before the other
       tests are applied 
    - Reduces
      the number of other statistical tests. 
   - E.g
       the [Scott-Knot](../gloss/sk.md) test.


