---
layout: post
title: 'What does research really tell us about deplatforming?'
date: 2022-06-20
permalink: /posts/2022/06/deplatforming
name_file: "2022-05-deplatforming"
lead:  "Merriam-Webster has defined Deplatforming as an 'attempt to boycott a group or individual through removing the platforms (such as speaking venues or websites) used to share information or ideas'"
csl: alpha.csl
numbersections: true
section-divs: true
link-citations: true
---

Merriam-Webster has defined Deplatforming as an *``attempt to boycott a group or individual through removing the platforms (such as speaking venues or websites) used to share information or ideas''* @meriamwebster_good_2018.
Prominent cases of deplatforming in social media include the banning of:
1) Toxic subreddits (standalone communities hosted within the Reddit social network) like r/FatPeopleHate, r/ChapoTrapHouse, and r/The\_Donald.
2) Accounts associated with far-right and conspiratorial communities like QAnon and the Alt-right. 
3) Influencers spousing far-right or conspiratorial beliefs like Alex Jones, Laura Loomer, and Milo Yiannopoulos.

Previous research has explored the effects of deplatforming, trying to characterize the effects of deplatforming broadly.
For instance, @chandrasekharan2017you studied how Reddit evolved circa 2015 after banning r/FatPeopleHate and r/CoonTown, two large toxic communities on the platform. 
They found that, within Reddit, a large percentage of users previously active in these communities stopped posting on the website and that those who continued drastically reduced their hate speech usage (as measured through a dictionary).
Also considering within-platform effects, @jhaver2021evaluating studied the banning of three high-profile influences on Twitter. 
Considering users that previously engaged with these accounts, they again found a decrease in the activity and toxicity (as measured through Google's Perspective API).

These within-platform studies are limited as they analyze the specific social networks where deplatforming occurred. Still, deplatformed influencers and communities usually migrate to alternative social networks or standalone websites. 
For instance, banned influencers like Alex Jones continued to be active on Gab @allyn_social_2021 (an alt-tech social media similar to Twitter) and used Telegram to broadcast content @rogers2020deplatforming; Communities like Fat People Hate migrated to Voat @mekacher2022can (a now-defunct Reddit clone); and r/The\_Donald even went as far as creating their own standalone social media, patriots.win @horta2021platform (formerly thedonald.win). 

Other papers address this limitation by studying pairs of social media platforms. 
@urman2022they found that far-right Telegram groups experienced explosive growth coinciding with the banning of far-right actors on mainstream social media platforms. 
@ali2021understanding developed a method for identifying the same user across different pairs of social networks -- Twitter and Gab, and Reddit and Gab. They find that the activity and toxicity of these users grow on Gab when they get banned on Twitter or Reddit (although their reach declines). Subsequent work found largely the same effects @mitts2021banned.
@horta2021platform studied the banning of two prominent Reddit communities that went on to create standalone websites: r/The\_Donald and r/Incels. 
They found that activity decreased for both communities following the platform migration but that toxicity (as measured by Perspective API) increased only for The Donald (perhaps due to the cryptic language used in Incel communities).
@rauchfleisch2021deplatforming studied the migration of deplatformed YouTube channels to Bitchute, finding that they receive drastically fewer views on the latter.

These across-platform studies cast doubt on the effectiveness of deplatforming. Overall activity and reach decrease in newer platforms @horta2021platform @ali2021understanding and in the platforms that carried out deplatformed, as pointed out by within-platform studies. However, there seems to be substantial migration to alternative platforms where hate speech runs rampant @freelon2020false, and users that migrate become more toxic @horta2021platform @ali2021understanding --- this is done considering matched users, so self-selection does not explain this effect. 
These results suggest a trade-off: deplatforming may lead to more toxic communities that are also smaller and have less reach.

Nonetheless, this work must also be considered with a grain of salt. First, most these studies only consider *active engagement traces* --- likes, comments, posts, etc. It may very well be that the number of lurkers (i.e., users who consume content but do not actively engage in the discussions) increases on fringe platforms, given that they often allow full access without registration. In that context, previous work may be underestimating the reach and (passive) user activity in alt-tech social media platforms.
Further, these studies consider unilateral migratory movements; they track how users banned in a specific mainstream platform behave on another specific fringe platform. However, there is no good reason to believe that users would not spread the time they previously spent on Reddit or Twitter across a variety of other platforms -- including less public-facing ones like Telegram or Discord @rogers2020deplatforming @urman2022they @conway_right-wing_2019.

Last and more subtly, the work discussed here papers are also limited in that they do not consider or model network effects.
It is well known that the utility of social media depends on the number of users @luca2015user --- thus, it is naïve to conclude that the effects of banning controversial opinions would be constant.
As Gab, Parler, and others receive more migrants, their utility will likely increase. Thus, it is tricky to generalize the effect of the bans on specific influencers and communities.
