---
layout: post
title: 'Effects of social recommendation'
date: 2022-03-28
permalink: /posts/2022/05/Social-Recommendations
name_file: "2022-05-srec"
lead:  "People recommender systems are widely used to suggest connections between users in social networks but are becoming pervasive across other areas (e.g., expert finding, education, dating, and employment). Analyses done on Twitter and Social Blue."
csl: alpha.csl
numbersections: true
section-divs: true
link-citations: true
...


People recommender systems are widely used to suggest connections between users in social networks but are becoming pervasive across other areas (e.g., expert finding @spaeth2013combining, education @vassileva2016small, dating @pizzato2013recommending, and  employment @almalis2015fodra). Analyses done on Twitter @su2016effect and Social Blue @daly2010network data indicate that these recommender systems impact the structure of social networks, favoring individuals who are already popular. 
In that context, researchers have questioned whether social recommender systems may exacerbate existing disparities [@fabbri2022exposure;@stoica2018algorithmic], e.g., increasing the social capital gap between majority and minority groups.

In the absence of recommender systems, previous work explored how the growth mechanisms of social networks (e.g., homophily, rich get richer, and minority majority partitions) can lead to a "glass ceiling" effect where specific groups have less "success" in the network [@avin2015homophily; @karimi2018homophily]. 
This theoretical work resonates with research showing bias against particular groups on platforms like Twitter @nilizadeh2016twitter, Fiverr @hannak2017bias, and AirBnB @edelman2017racial.

Recommendation algorithms may intensify the disadvantage of minority groups, an effect which @stoica2018algorithmic call the  "*algorithmic* glass ceiling."
Under a specific random walk recommender system and strong assumptions, @stoica2018algorithmic find that differentiated homophily ("two groups exhibiting varying propensity to favor their own peers") can lead recommender systems to exacerbate the "glass ceiling" effect already present in social networks.
The notion of differentiated homophily also helps to explain the apparent contradiction that the glass ceiling can act upon groups that are majorities (women on Instagram).


@fabbri2022exposure introduce a model to simulate the feedback loop between users and contact recommendation algorithms (e.g., who to follow). They find that link recommenders exacerbate "rich-get-richer" effects and provide disparate exposure to minority homophilic groups. 
This work largely confirms simulation-based results from previous work considering one round of recommendations @fabbri2020effect, and theoretical insights from @stoica2018algorithmic.


Empirical evidence measuring the magnitude of the effect of the "algorithmic glass ceiling effect" is lacking --- perhaps because it may be difficult to disentangle it from the "natural" glass ceiling effect that can occur as social networks grow @avin2015homophily. 
In that sense, this literature would benefit from empirical experimental or quasi-experimental work that attempts to measure the effects of social recommendation in the wild.
Also, proposed solutions to the "algorithmic ceiling" are not deeply explored (although some ideas are mentioned in @stoica2018algorithmic and @karimi2018homophily) and seem hard to apply in the deep-learning-based recommender systems often employed in large social networks @covington2016deep. Upcoming work could also measure the extent to which these approaches can have a real-world impact.



## References

---
