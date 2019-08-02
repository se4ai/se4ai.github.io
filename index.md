---
title: " Preface"
layout: default
---

It is the ethical duty of anyone building
AI software   to produce tools  that conform to accepted ethical standards.
This book discusses how that might be done.

It is important, and timely, to take more time to talk about ethics.
The more society uses software to mediate its activities, and the more it uses 
artificial intelligence
to control that software, the more we need to consider the ethical implications 
 of those systems.

Happily, AI can help with ethics. 
Ethics is all about choice. Ethical principles guide the choices we make
and how we evaluate each choice.
When applying AI tools (such as data miners,
optimizers, or theorem provers), developers can make many choices:

- what goals are required;
- how to represent and apply domain knowledge
- what data to use 
- how to best weight  different examples or different attributes, 
- what algorithms  to apply for the learning;
- what optimizers to apply to better (e.g.) tune the learners;

To understand that, consider one view
of how AI converts data into conclusions:

```
data -> AI tool -> conclusion
```

This view is very misleading since it ignores all the choices inside AI tools
(and how those choices effect the resulting conclusions).
There are many ways that  AI can combine data and data miners and optimizers and theorem provers.
Each of these methods produces its own model,
only some of
which do we choose to apply[^choice]:

```
data -> AI tool --> |--> model1  \
        (control    |--> model2   \
       settings)    |--> model3    |--> choice --> model --> conclusion
                    |--> model4   /
                    |--> etc     /
```

[^choice]: This is not to say that AI just makes things up. While data may lead to multiple models, there are many models not supported by any data.  So one way to look at AI is a method to  quickly rule out was is definitely wrong (and then help us faster explore what is left).  As [Karl Popper](REFS#popper-1963) said, the ideas that we most believe are the ones that have survived the most attempts at refutation.  This view of science-as-refutation has a  long history.  Wolfgang Pauli was a prominent physics in the first half of the 20th century.  When reading a  paper of another physicist, he famously remarked "Das ist nicht nur nicht richtig; es ist nicht einmal falsch!" ( That's not just not right; it is not even wrong!).  


Each  model generated  by AI represents a trade between
what we want;
and what we want to avoid.
The key to ethical AI software is controlling what  choices are made during the software construction process. AI
technologies are unique in that, for the first time in human history, we can use AI to help us make those choices.
As shown in this book,
using data miners and optimizers and theorem provers, we can select the kinds of models we want.
Hence we say that

- _Ethics_ are a choice;
- And
_not choosing is unethical_
since we are not
controlling 
what goals are not satisfied by our AI tools.


To understand those choices, we need to understand more about the technologies used with AI tools.
When used together, 
data miners,
optimizers, and 
theorem provers
can greatly benefit each other.
Data miners can simplify optimizers. Optimizers can make theorem provers run faster.
Theorem provers can become generators for data mining.
But more importantly, each can be used to control the choices made by the other.
Also, when properly controlled, those choices can be made to achieve ethical goals.

The book introduces these technologies, from a programming perspective.
Our goal is to give you enough information so you can build, refactor, and improve  your own versions of these tools.

This book also asks what is missing from most other textbooks on AI and SE.
To fill that gap,  we will cover:

- Software processes:
Software process is how large teams divide tasks such that more people can deliver more functionality, faster.
Software processes are vital to the scalability and maintainability of AI tools.
- Ethically-aligned design:
This is how match up high-level ethical goals (e.g. fairness, reliability, transparency, etc)  with
lower-level functionality (e.g. rule generation, anomaly detection, clustering, etc). 

