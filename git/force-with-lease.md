    git push --force-with-lease

What --force-with-lease does is refuse to update a branch unless it is the state that we expect; i.e. nobody has updated the branch upstream. In practice this works by checking that the upstream ref is what we expect, because refs are hashes, and implicitly encode the chain of parents into their value.

ref:
<br />https://developer.atlassian.com/blog/2015/04/force-with-lease/
<br />https://robots.thoughtbot.com/git-push-force-with-lease 