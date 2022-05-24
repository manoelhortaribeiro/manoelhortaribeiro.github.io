---
bibliography: 2022-05-24-Social-Recommendations.bib
csl: alpha.csl
date: 2022-03-28
layout: post
lead: People recommender systems are widely used to suggest connections
  between users in social networks but are becoming pervasive across
  other areas (e.g., expert finding, education, dating, and employment).
  Analyses done on Twitter and Social Blue.
link-citations: true
name_file: 2022-05-srec
numbersections: true
permalink: /posts/2022/05/Social-Recommendations
section-divs: true
title: Effects of social recommendation
---

People recommender systems are widely used to suggest connections
between users in social networks but are becoming pervasive across other
areas (e.g., expert finding \[[SpDe13](#ref-spaeth2013combining)\],
education \[[VaMcGr16](#ref-vassileva2016small)\], dating
\[[PRAK13](#ref-pizzato2013recommending)\], and employment
\[[ATKS15](#ref-almalis2015fodra)\]). Analyses done on Twitter
\[[SuShGo16](#ref-su2016effect)\] and Social Blue
\[[DaGeMi10](#ref-daly2010network)\] data indicate that these
recommender systems impact the structure of social networks, favoring
individuals who are already popular. In that context, researchers have
questioned whether social recommender systems may exacerbate existing
disparities \[[FCBC22](#ref-fabbri2022exposure);
[StRiCh18](#ref-stoica2018algorithmic)\], e.g., increasing the social
capital gap between majority and minority groups.

In the absence of recommender systems, previous work explored how the
growth mechanisms of social networks (e.g., homophily, rich get richer,
and minority majority partitions) can lead to a “glass ceiling” effect
where specific groups have less “success” in the network
\[[AKLM15](#ref-avin2015homophily);
[KGWS18](#ref-karimi2018homophily)\]. This theoretical work resonates
with research showing bias against particular groups on platforms like
Twitter \[[NGLD16](#ref-nilizadeh2016twitter)\], Fiverr
\[[HWGM17](#ref-hannak2017bias)\], and AirBnB
\[[EdLuSv17](#ref-edelman2017racial)\].

Recommendation algorithms may intensify the disadvantage of minority
groups, an effect which \[[StRiCh18](#ref-stoica2018algorithmic)\] call
the “*algorithmic* glass ceiling.” Under a specific random walk
recommender system and strong assumptions,
\[[StRiCh18](#ref-stoica2018algorithmic)\] find that differentiated
homophily (“two groups exhibiting varying propensity to favor their own
peers”) can lead recommender systems to exacerbate the “glass ceiling”
effect already present in social networks. The notion of differentiated
homophily also helps to explain the apparent contradiction that the
glass ceiling can act upon groups that are majorities (women on
Instagram).

\[[FCBC22](#ref-fabbri2022exposure)\] introduce a model to simulate the
feedback loop between users and contact recommendation algorithms (e.g.,
who to follow). They find that link recommenders exacerbate
“rich-get-richer” effects and provide disparate exposure to minority
homophilic groups. This work largely confirms simulation-based results
from previous work considering one round of recommendations
\[[FBBC20](#ref-fabbri2020effect)\], and theoretical insights from
\[[StRiCh18](#ref-stoica2018algorithmic)\].

Empirical evidence measuring the magnitude of the effect of the
“algorithmic glass ceiling effect” is lacking — perhaps because it may
be difficult to disentangle it from the “natural” glass ceiling effect
that can occur as social networks grow
\[[AKLM15](#ref-avin2015homophily)\]. In that sense, this literature
would benefit from empirical experimental or quasi-experimental work
that attempts to measure the effects of social recommendation in the
wild. Also, proposed solutions to the “algorithmic ceiling” are not
deeply explored (although some ideas are mentioned in
\[[StRiCh18](#ref-stoica2018algorithmic)\] and
\[[KGWS18](#ref-karimi2018homophily)\]) and seem hard to apply in the
deep-learning-based recommender systems often employed in large social
networks \[[CoAdSa16](#ref-covington2016deep)\]. Upcoming work could
also measure the extent to which these approaches can have a real-world
impact.

## References

------------------------------------------------------------------------

<div id="refs" class="references csl-bib-body" markdown="1">

<div id="ref-avin2015homophily" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[AKLM15\] </span><span
class="csl-right-inline"><span class="smallcaps">Avin, Chen</span> ;
<span class="smallcaps">Keller, Barbara</span> ; <span
class="smallcaps">Lotker, Zvi</span> ; <span class="smallcaps">Mathieu,
Claire</span> ; <span class="smallcaps">Peleg, David</span> ; <span
class="smallcaps">Pignolet, Yvonne-Anne</span>: Homophily and the glass
ceiling effect in social networks. In: *Proceedings of the Conference on
Innovations in Theoretical Computer Science*, 2015</span>

</div>

<div id="ref-almalis2015fodra" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[ATKS15\] </span><span
class="csl-right-inline"><span class="smallcaps">Almalis, Nikolaos
D</span> ; <span class="smallcaps">Tsihrintzis, George A</span> ; <span
class="smallcaps">Karagiannis, Nikolaos</span> ; <span
class="smallcaps">Strati, Aggeliki D</span>: FoDRA—A new content-based
job recommendation algorithm for job seeking and recruiting. In:
*Procceedings of the International Conference on Information,
Intelligence, Systems and Applications* : IEEE, 2015</span>

</div>

<div id="ref-covington2016deep" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[CoAdSa16\] </span><span
class="csl-right-inline"><span class="smallcaps">Covington, Paul</span>
; <span class="smallcaps">Adams, Jay</span> ; <span
class="smallcaps">Sargin, Emre</span>: Deep neural networks for youtube
recommendations. In: *Proceedings of the 10th ACM conference on
recommender systems*, 2016, S. 191–198</span>

</div>

<div id="ref-daly2010network" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[DaGeMi10\] </span><span
class="csl-right-inline"><span class="smallcaps">Daly, Elizabeth
M</span> ; <span class="smallcaps">Geyer, Werner</span> ; <span
class="smallcaps">Millen, David R</span>: The network effects of
recommending social connections. In: *Proceedings of the ACM Conference
on Recommender Systems*, 2010</span>

</div>

<div id="ref-edelman2017racial" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[EdLuSv17\] </span><span
class="csl-right-inline"><span class="smallcaps">Edelman,
Benjamin</span> ; <span class="smallcaps">Luca, Michael</span> ; <span
class="smallcaps">Svirsky, Dan</span>: Racial discrimination in the
sharing economy: Evidence from a field experiment. In: *American
Economic Journal: Applied Economics* Bd. 9 (2017), Nr. 2, S. 1–22</span>

</div>

<div id="ref-fabbri2020effect" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[FBBC20\] </span><span
class="csl-right-inline"><span class="smallcaps">Fabbri,
Francesco</span> ; <span class="smallcaps">Bonchi, Francesco</span> ;
<span class="smallcaps">Boratto, Ludovico</span> ; <span
class="smallcaps">Castillo, Carlos</span>: The effect of homophily on
disparate visibility of minorities in people recommender systems. In:
*Proceedings of the International AAAI Conference on Web and Social
Media*, 2020</span>

</div>

<div id="ref-fabbri2022exposure" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[FCBC22\] </span><span
class="csl-right-inline"><span class="smallcaps">Fabbri,
Francesco</span> ; <span class="smallcaps">Croci, Maria Luisa</span> ;
<span class="smallcaps">Bonchi, Francesco</span> ; <span
class="smallcaps">Castillo, Carlos</span>: Exposure Inequality in People
Recommender Systems: The Long-Term Effects. In: *Proceedings of the
International AAAI Conference on Web and Social Media*, 2022</span>

</div>

<div id="ref-hannak2017bias" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[HWGM17\] </span><span
class="csl-right-inline"><span class="smallcaps">Hannák, Anikó</span> ;
<span class="smallcaps">Wagner, Claudia</span> ; <span
class="smallcaps">Garcia, David</span> ; <span
class="smallcaps">Mislove, Alan</span> ; <span
class="smallcaps">Strohmaier, Markus</span> ; <span
class="smallcaps">Wilson, Christo</span>: Bias in online freelance
marketplaces: Evidence from taskrabbit and fiverr. In: *Proceedings of
the ACM Conference on Computer Supported Cooperative Work and Social
Computing*, 2017</span>

</div>

<div id="ref-karimi2018homophily" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[KGWS18\] </span><span
class="csl-right-inline"><span class="smallcaps">Karimi, Fariba</span> ;
<span class="smallcaps">Génois, Mathieu</span> ; <span
class="smallcaps">Wagner, Claudia</span> ; <span
class="smallcaps">Singer, Philipp</span> ; <span
class="smallcaps">Strohmaier, Markus</span>: Homophily influences
ranking of minorities in social networks. In: *Scientific reports* Bd.
8, Nature Publishing Group (2018), Nr. 1</span>

</div>

<div id="ref-nilizadeh2016twitter" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[NGLD16\] </span><span
class="csl-right-inline"><span class="smallcaps">Nilizadeh,
Shirin</span> ; <span class="smallcaps">Groggel, Anne</span> ; <span
class="smallcaps">Lista, Peter</span> ; <span class="smallcaps">Das,
Srijita</span> ; <span class="smallcaps">Ahn, Yong-Yeol</span> ; <span
class="smallcaps">Kapadia, Apu</span> ; <span class="smallcaps">Rojas,
Fabio</span>: Twitter’s glass ceiling: The effect of perceived gender on
online visibility. In: *Proceedings of the International AAAI Conference
on Web and Social Media*, 2016</span>

</div>

<div id="ref-pizzato2013recommending" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[PRAK13\] </span><span
class="csl-right-inline"><span class="smallcaps">Pizzato, Luiz</span> ;
<span class="smallcaps">Rej, Tomasz</span> ; <span
class="smallcaps">Akehurst, Joshua</span> ; <span
class="smallcaps">Koprinska, Irena</span> ; <span
class="smallcaps">Yacef, Kalina</span> ; <span class="smallcaps">Kay,
Judy</span>: Recommending people to people: the nature of reciprocal
recommenders with a case study in online dating. In: *User Modeling and
User-Adapted Interaction* Bd. 23, Springer (2013), Nr. 5,
S. 447–488</span>

</div>

<div id="ref-spaeth2013combining" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[SpDe13\] </span><span
class="csl-right-inline"><span class="smallcaps">Spaeth,
Alexandre</span> ; <span class="smallcaps">Desmarais, Michel C</span>:
Combining collaborative filtering and text similarity for expert profile
recommendations in social websites. In: *Procceedings of the
International Conference on User Modeling, Adaptation, and
Personalization*, 2013</span>

</div>

<div id="ref-stoica2018algorithmic" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[StRiCh18\] </span><span
class="csl-right-inline"><span class="smallcaps">Stoica,
Ana-Andreea</span> ; <span class="smallcaps">Riederer,
Christopher</span> ; <span class="smallcaps">Chaintreau,
Augustin</span>: Algorithmic Glass Ceiling in Social Networks: The
effects of social recommendations on network diversity. In: *Proceedings
of the World Wide Web Conference*, 2018</span>

</div>

<div id="ref-su2016effect" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[SuShGo16\] </span><span
class="csl-right-inline"><span class="smallcaps">Su, Jessica</span> ;
<span class="smallcaps">Sharma, Aneesh</span> ; <span
class="smallcaps">Goel, Sharad</span>: The effect of recommendations on
network structure. In: *Proceedings of the International Conference on
World Wide Web*, 2016</span>

</div>

<div id="ref-vassileva2016small" class="csl-entry" markdown="1">

<span class="csl-left-margin">\[VaMcGr16\] </span><span
class="csl-right-inline"><span class="smallcaps">Vassileva,
Julita</span> ; <span class="smallcaps">McCalla, Gordon I</span> ; <span
class="smallcaps">Greer, Jim E</span>: From small seeds grow fruitful
trees: How the PHelpS peer help system stimulated a diverse and
innovative research agenda over 15 years. In: *International Journal of
Artificial Intelligence in Education* Bd. 26, Springer (2016), Nr. 1,
S. 431–447</span>

</div>

</div>
