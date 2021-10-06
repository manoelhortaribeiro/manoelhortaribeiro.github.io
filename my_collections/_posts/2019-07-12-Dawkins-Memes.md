---
layout: post
title: 'On Internet Memes and What Dawkins Meant by Memes'
date: 2019-07-12
permalink: /posts/2019/06/dawkins-memes
tags:
  - memes
  - online-social-networks
name_file: "2019-07-12-Dawkins-Memes"

lead: "This is probably the most “daring” blog post I wrote as it touches on subjects I’m not an expert on. However, the idea of studying memes (the meme of studying memes?) is widespread among CS and network science, often more than not by people that do not have studied evolutionary biology or social sciences. Thus I think the adventure is worthwhile."
---

---

This is probably the most “daring” blog post I wrote as it touches on subjects I’m not an expert on. However, the idea of studying memes (the meme of studying memes?) is widespread among CS and network science, often more than not by people that do not have studied evolutionary biology or social sciences. Thus I think the adventure is worthwhile. 


<img src="{{ site.baseurl }}/images/2019-07-12-Dawkins-Memes/dawkins_meme.jpg" >
<em>I actually found this online</em>

## On Dawkinian Memes


In 1976, years before the internet, Richard Dawkins coined the term meme in its book [“The Selfish Gene”](https://en.wikipedia.org/wiki/The_Selfish_Gene). Dawkins, who later rose to fame due to his (somewhat aggressive) atheist activism, proposed that a meme was like a gene, but for information. The comparison to a gene should be taken into consideration given the context of the book. There, Dawkins argues that the gene, and not the individual or the species, was the fundamental unit of evolution, and that things like self-sacrifice and empathy could be explained by thinking of living beings as "gene survival machines", whose driving purpose was to pass on our genes.

<img src="{{ site.baseurl }}/images/2019-07-12-Dawkins-Memes/The_Selfish_Gene3.jpg" >
<em>Original cover of the book :)</em>

To Dawkins, memes are to minds what genes are to organisms: replicators that employ vehicles. A good example here is religion. It is not encoded in our DNA, yet it can be replicated from individual to individual (fecundity), it morphs itself as it propagates (variation), its success depends on its characteristics (fitness), etc. Overall, the cultural evolution of ideas seems to fit the theory of the evolution of replicators under natural selection.

## Problems with Dawkinian Memes

We highlight problems with the concept of memes, presented in [“The Trouble with Memes”, by Scott Atran](https://link.springer.com/content/pdf/10.1007/s12110-001-1003-0.pdf
): the lack of an operational definition, the hardship of distinguishing between mimicking and inference.

Although it is hard to define exactly what constitutes a gene, as Dawkins point outs, there is a straightforward and operational definition. DNA-encoded units of information map into discrete (e.g. biological gender) and continuous (e.g. height). This is not the same with memes. Given that some idea or behavior became widespread, it is arbitrary to pinpoint the scope of this idea or of this behavior. For example, if we consider the spread of a normative passage of the Bible, "Thou shall not kill". When this is spread, what exactly is going through selection? Is it the particular set of words? Is it the concept these words bring? Is it the religions associated with this words? Is it the concept of religion in general, where you have rules for how people should behave? It is simply not clear, and the possibility to shift between these countless levels of abstraction could allow for tremendous cherry-picking. 

This is not where this definition problem ends.
Like genes, memes interact with multiple other memes (the success of an meme in spreading depends on all other memes in the individuals, just like with genes). For genes, when phenotype (e.g. a disease) is associated with a very specific gene, it is easy to track it. However, to find association between genes and some traits which are influenced by many genes is very tricky. In fact, it is a research problem that lies in the forefront of the research in causality and of statistical modelling. For memes, nevertheless, this problem seems even more dire, as there, we would need not only this intricate causal structure between which memes influence some phenomena, but also to determine what these memes _are_. 


Lastly, another interesting point by Atran is how, given the definition of meme, it may be impossible to distinguish between ideas that evolved from each other (e.g. Romeo and Juliet influenced countless other stories) from ideas that co-evolved (e.g. creation myths that replicate patterns across cultures, ideas for basic tools that occurred in different societies). Here, a particularly interesting parallel with biology is that, there, often species were categorized as being very close evolution-wise by looking at their phenotype, but then, after more advanced techniques were developed, their genes showed that they are not close in the forking paths of evolution, but that it just happened that they co-evolved similarly. 



## Memes in Pop Culture, Computer Science and Network Science

The concept of memes has flourished in pop culture and in fields like CS and Network Science. "For the masses", memes is a synonym of activities (e.g. [Ice Bucket Challenge](https://knowyourmeme.com/memes/ice-bucket-challenge)), concepts (e.g. [Clown world](https://knowyourmeme.com/memes/clown-pepe-honk-honk-clown-world)), catchphrases (e.g. MAGA) or pieces of media (e.g. [Pepe](https://knowyourmeme.com/memes/pepe-the-frog)) that spread via the internet. This concept also is adopted in academia, for example, [when 
Savvas and the folks at iDrama studied the influence of fringe communities in the "meme environment" of the internet](https://arxiv.org/abs/1805.12512), or in [Meme-tracking and the Dynamics of the News Cycle](https://dl.acm.org/citation.cfm?id=1557077), where Leskovec, Backstrom and Kleimberg track short, distinctive phrases as they travel through the news.
 In both cases, "meme" is used by academics as a "trackable information unit". This idea is also implied in the information diffusion literature (think [independent cascades models](https://link.springer.com/article/10.1023/A:1011122126881), and [linear thresholds models](https://www.journals.uchicago.edu/doi/abs/10.1086/226707)), that often not call these trackable units memes, but could very well do so.
 
 
<img src="{{ site.baseurl }}/images/2019-07-12-Dawkins-Memes/rare_pepe.jpg" >
<em>A rare pepe the frog</em>

 Previously, we have seen that a big challenge for the proponents of memetics was to operationalize the concept of a meme. Here we can clearly see how our community did so. They removed some of the core aspects of the original idea of meme:
 
1. Firstly, the study of memes in large scale online accounts for very little *variation*. There is no room for major changes in the information as it diffuses in most of existing work. Information is often considered atomic, and when not, tracking it relies on comparing strings or pixels, and not the semantics behind ideas. Moreover, information is not considered hierarchically, a given level of abstraction (sentences, images) is set and this is what it is. A direct consequence of this is that the scope of which memes we were able to study was greatly reduced to those where tracking was trivial through pattern matching, we limit our study to cascades where a given images where propagated (e.g. as in [Do Cascades Recur?](https://dl.acm.org/citation.cfm?id=2882993)), or a given text string (e.g. as in the previously mentioned [Meme-tracking and the Dynamics of the News Cycle](https://dl.acm.org/citation.cfm?id=1557077)). 

2. Secondly, there is no sense of fitness of a meme in an evolutionary sense. Memes are considered something with a definite life-span, not something that would perpetuate itself forever (perhaps due to the very low-level abstractions that we are able to pattern match). There may even be some notion of "competing information cascades", such as in [Clash of the Contagions](http://dx.doi.org/10.1109/ICDM.2012.159), a nice paper by Myers and Leskovec, but there is no notion that these ideas are struggling to perpetuate themselves in the minds of users, or of how these ideas "compete for users" in more sophisticated ways. 

If we expand beyond the first challenge, we still risk being stuck at the same problems that the original Dawkinian memes had. The ill-definition problem would surface once the exact pattern matching and the allowance for variation is not there, and so would the hardship between distinguishing between mimicry and inference. Yet, there seems to be somewhere to go exploring the second limitation that existing work has: not considering information in a competitive natural-selection-esque environment. In the age of content creators struggling for our attention, studying how information "competes" for us in algorithmically rich environments seems to be a way to go.

