---
layout: post
title: 'Do Platform Migrations Compromise Content Moderation?'
date: 2021-10-06
permalink: /posts/2021/10/deplatforming

name_file: "2021-10-01-Deplatforming"

lead:  "In 2018, around the time when America's leading conspiracy theorist was banned from YouTube, Apple, and 
Facebook, Merriam-Webster noted that a shiny new verb was emerging —to deplatform, 
the attempt to boycott a group or individual through removing the platforms (such as speaking venues or websites) used
 to share information or ideas."
---

---

In 2018, around the time when America's leading conspiracy theorist<sup>1</sup> was banned from YouTube, Apple, and 
Facebook,<sup>2</sup> Merriam-Webster noted that a shiny new verb was emerging —'*to deplatform*' (/diːˈplatfɔːm/), 
"the attempt to boycott a group or individual through removing the platforms (such as speaking venues or websites) used
 to share information or ideas."<sup>3</sup>  
The practice has become increasingly prevalent in social media, particularly in the context of right-wing extremism<sup>4</sup> and
 of conspiracy theories around COVID-19.<sup>5</sup>
 And every time a new personality or a community is kicked out of a new platform, two questions are reignited:
  
- Should we deplatform?

- What happens after we deplatform?

The first question is tightly related to debates on the limits of free speech and on the legitimacy of big tech to 
enforce moderation decisions.<sup>6</sup> 
Yet from a pragmatic perspective, its answer is highly dependent on the second question.... 
After a group gets 'deplatformed' from a given social media site they can choose to participate in other communities within the 
same platform **or** they can migrate to an alternative, possibly fringe platform (or platforms) where their behavior
is considered acceptable. In both scenarios, things could backfire...

<br />
<img src="{{ site.baseurl }}/images/2021-10-01-Deplatforming/F1.png" width="400px" >
<em>Illustration of how things could backfire...</em>
<br />

- **Concern #1:** If users migrate to other communities within the same platform, their problematic behavior/content may also migrate 
to other communities (existing or newly created) within the same platform. 

- **Concern #2:** If users migrate to an alternate platform, the ban could unintentionally strengthen a fringe platform 
(e.g., 4chan or Gab) where problematic content goes largely unmoderated.<sup>9</sup> From the new platform, the harms 
inflicted by the toxic community on society could be even higher.


Previous work has largely addressed concern #1, showing that users who remained on Reddit after the banning of 
several communities in 2015 drastically reduced their usage of hate speech and that counter-actions taken by users from
 the banned communities were promptly neutralized.<sup>7,8</sup> In our latest [CSCW paper][paper], we 
 set out to explore what happens in the second scenario: when users change platforms.

## What we did

We focused on the case when users migrate (mostly) to a single alternate platform. This has happened with two
prominent Reddit communities, r/The_Donald, which migrated to the standalone website thedonald.win (now patriots.win),
and r/Incels, which migrated to the incels.co forum. Importantly, these migrations were "official," in the
sense that they had the backing of community leaders of the subreddit.
 In the case of /r/TheDonald, for instance, the community was locked for weeks, and the moderators managed to
 pin a post containing a link to the alternate platform.

<br />
<img src="{{ site.baseurl }}/images/2021-10-01-Deplatforming/F2.png" width="500px" >
<em>Timeline of the deplatforming of r/The_Donald.</em>
<br />

We analyzed how these two communities progressed in two dimensions. First, we looked at their *activity,* considering
how the number of posts, users and newcomers changed with the migration. Second, we looked at text-derived signals such
 as Toxicity Scores (thanks, Perspective API!) that would indicate *user radicalization* in these communities. 
With these signals, we showed that deplatforming a community significantly decreases community-level
 activity in both r/The_Donald and r/Incels. For r/The_Donald, we also find that it significantly increased 
 radicalization-related signals.
 
 <br />
<img src="{{ site.baseurl }}/images/2021-10-01-Deplatforming/F3.png" width="500px" >
<em>User-level effects of the migration in r/The_Donald. 
</em>
<br />

In the Figure above, we showcase part of our results for r/The_Donald. For each signal, in the y-axis, we show the average user log-2-ratio (x-axis).
To calculate this value we:
(i) match users before and after the migration and;
(ii) calculate the average value for each user in the 90 days before and after the migration. 
Then, we divide the average value post-migration (e.g., the number of posts a day a user had in 
thedonald.win) by the average value pre-migration (e.g., the average value of posts a day a user had in /r/The_Donald).
Lastly, we take the log2 of this ratio to make the value interpretable. 
For instance, if the log-2-ratio of the number of posts per user is 1, 
it means that the user posted twice as much in platform 2 when compared to platform 1. 
If it's -2, it means that the user posted 4 times less in platform 2.

In that context, we can see in the figure that the banning of r/The_Donald led to a reduction in posts of around 40% (roughly equal to 1 - 2<sup>0.8</sup>),
and to an increase in Toxicity (as measured by Perspective API) of around 31%. 
In the paper, we also run other analyses on a community-level that yield largely the same results.
 
## So what?

Our analysis suggests that community-level moderation measures decrease the
capacity of toxic communities to retain their activity levels and attract new members, **but that
this may come at the expense of making these communities more toxic and ideologically radical.**

As platforms moderate, they should consider their impact not only on their own websites
and services, but in the context of the Web as a whole. Toxic communities respect no platform
boundary, and thus, platforms should consider being more proactive in identifying and sanctioning
toxic communities before they have the critical mass to migrate to a standalone website.


[<sup>1</sup>]: https://nymag.com/intelligencer/2013/11/alex-jones-americas-top-conspiracy-theorist.html
[<sup>2</sup>]: https://www.vox.com/2018/8/6/17655658/alex-jones-facebook-youtube-conspiracy-theories
[<sup>3</sup>]: https://www.vox.com/2018/8/6/17655658/alex-jones-facebook-youtube-conspiracy-theories
[<sup>4</sup>]: https://www.forbes.com/sites/jackbrewster/2021/01/12/the-extremists-conspiracy-theorists-and-conservative-stars-banned-from-social-media-following-the-capitol-takeover/
[<sup>5</sup>]: https://edition.cnn.com/2021/09/01/tech/reddit-covid-misinformation-ban/index.html
[paper]: https://arxiv.org/pdf/2010.10397.pdf

## References
1. https://nymag.com/intelligencer/2013/11/alex-jones-americas-top-conspiracy-theorist.html 
2. https://www.vox.com/2018/8/6/17655658/alex-jones-facebook-youtube-conspiracy-theories 
3. https://www.merriam-webster.com/words-at-play/the-good-the-bad-the-semantically-imprecise-08102018 
4. https://www.forbes.com/sites/jackbrewster/2021/01/12/the-extremists-conspiracy-theorists-and-conservative-stars-banned-from-social-media-following-the-capitol-takeover/ 
5. https://edition.cnn.com/2021/09/01/tech/reddit-covid-misinformation-ban/index.html 
6. Almeida, V., Filgueiras, F., and Gaetani, F. Digital governance and the tragedy of the commons. IEEE Internet Computing (2020).
7. Chandrasekharan, E., Pavalanathan, U., Srinivasan, A., Glynn, A., Eisenstein, J., and Gilbert, E. You can’t stay
here: the efficacy of Reddit’s 2015 ban examined through hate speech. In Proceedings of the ACM on Human-Computer
Interaction (CSCW) (2017). 
8. Saleem, H. M., and Ruths, D. The aftermath of disbanding an online hateful community. arXiv:1804.07354 (2018).
9. Mathew, B., Illendula, A., Saha, P., Sarkar, S., Goyal, P., and Mukherjee, A. Hate begets hate: a temporal study
of hate speech. In Proceedings of the ACM on Human-Computer Interaction (CSCW) (2020).
10. Previously shown to be related to radicalization, see: Pennebaker, J. W., and Chung, C. K. Computerized text analysis of Al-Qaeda transcripts. A content analysis reader
(2007).
