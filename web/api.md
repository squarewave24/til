# API

## Idempotence

popular in REST api terminology. 

anecdote:
> https://twitter.com/rombulow/status/990684453734203392

it means, returning the same result EVERY TIME. 

a ```GET``` should be idempotent. 

a ```/get/toggle``` is NOT idempotent, because it does not return the same result. 

* also it looks like it probably has side effects which is not somehting you'd want from a ```get```