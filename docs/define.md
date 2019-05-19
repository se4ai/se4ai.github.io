---
title: Definitions
layout: default
---

## What is ...?

Before going any further, we'll need some preliminaries. For example,
what do we mean  by SE? By AI?

### What is SE?

Software engineering is the creation/ maintainance of some software
product of an acceptable standard, given the available resources (time,
people, tools, etc).

Software engineering should be (and often isn't) a process of looking
at current software so we can make it better.  Sometimes that means
adjusting it and sometimes that means burning it down and starting afresh.
Accroding to W. Edwards Deming[^1] (a promient writer on quality control),
this process is called _Plan, Do, Study, Act_.

Currently, software engineering is very, very good at _Do_ and _Act_. Many
software teams use practice continous integration. Such CI-teams can
build and deploy new versions of complex systems, several times per day.

Any number of other texts explore _doing_ and _acting_.  Here, we explore
_Plan_ and _Study_. This the process of:

- collecting and analying the data that lets us understand:
     - what the users want (the objectives);
     - what are the current options;
     - what are the constraints around those options.
- then making choices that:
     - reach as many objectives as we can;
     - as easily as possible;
     - while satisfying most of the contraints.

This means that SE in the age of AI
can use some combiantion of data mining and optimization:

- _Optimizers_ are algorithms
that take some model (or something)
and then try to learn inputs that lead to better results.
- Sometimes (often) there is no model in which
case they can be built via _data mining_.
- Whereas data miners usually explore a fixed
set of data, optimizers can generate more data by re-running the model 
many times,
using different inputs.
- Data miners, on the other hand,
reflect over data to return a
summary of that data.

One informal way to characterize the difference between data miners and optimizers is _slice_ versus _zoom_.

- Data miners _slice_  data such that similar patterns  are found within each division.
- Optimizers  _zoom_ into interesting regions of the data,
then then use a model to fill  in any missing details
about those regions. 

Having spent two decades building optimizers and data miners,
we assert that, internal to the code,
 data mining and optimizers are very similar.
Because of this underlying similarity, it is easy
to mix-and-match the services of data miners and optimizers,
in useful ways.
For example,

- When the optimizer is running too slowly, we might apply data mining
  to divide up and simpigy the problem, then run optimizers on 
  the simplified bits.
- Data miners are configured by many magic parameters. When we do not know
  what choices to apply, we ask optimizers to automatically
  explore those choices.

Next, we offer examples from software engineering where
data miners and optimizers have been mixed-and-matched in order
to better manage _Plan_ and _Study_.

### "No, no, that isn't SE"

To say the obvious, the above is just an opinion. And its an opinion that some people might disagree with.
For exampel:

"That's not SE. I know since I am a software engineer and the above says very little about my day to day work." 

To which we reply, that it might not characterize your day to day work... yet. But it will soon. SE keeps
redefining itself. There is a long history of people saying "X is not about" and yet, a decade later,
SE is all about X. Consider:


- SE is not about  users (Dijkstra, 79)[^2]
- SE is not about testing (Mills, 1985)[^3]
- SE is not about requirements (Paulk, 1993)[^4]
    - “Analysis and allocation of the system requirements is NOT the responsibility of the SE group but is a prerequisite for their work”
- SE is not about deployment (before CI)
- SE is not about AI... yet

Our point here is that even though AI is not a standard tool 
used and studied by 
software engineers, it will soon be. 

If you agree, then this site is for you.

Otherwise, send us your email and we'll check back in with you in 2020.

## Notes

[^1]: Aguayo, Rafael (1990). Dr. Deming: the American who taught the Japanese about quality. A Lyle Stuart book. Secaucus, NJ: Carol Pub. Group. p. 76. ISBN 978-0818405198. OCLC 22347078. Also published by Simon & Schuster, 1991.

[^2]: asdas
[^3]: asdas
[^4]: asdas

