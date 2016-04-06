[In probability theory, the multi-armed bandit problem is a problem in which a gambler at a row of slot machines (sometimes known as "one-armed bandits") has to decide which machines to play, how many times to play each machine and in which order to play them.](https://en.wikipedia.org/wiki/Multi-armed_bandit)

This problem has a solution that helps to allocate resources in a efficient way. 

There has been discussions comparing this algorithm to A/B testing method [here](https://vwo.com/blog/multi-armed-bandit-algorithm/) and [here](http://stevehanov.ca/blog/index.php?id=132), discussion [here](https://news.ycombinator.com/item?id=11437114).

In short, it splits resource utilization into 2 phases: Exploration (10% of tries) and Exploitation (90% of tries). The 10/90 can be tweaked, but the idea is to identify the better paying "machines" and use those the rest of time therefore maximizing profit.   

   