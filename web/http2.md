
## HTTP/2 multiplexed

HTTP/1.x has a problem called “head-of-line blocking,” where effectively only one request can be outstanding on a connection at a time.

HTTP/1.1 tried to fix this with pipelining, but it didn’t completely address the problem (a large or slow response can still block others behind it). Additionally, pipelining has been found very difficult to deploy, because many intermediaries and servers don’t process it correctly.

This forces clients to use a number of heuristics (often guessing) to determine what requests to put on which connection to the origin when; since it’s common for a page to load 10 times (or more) the number of available connections, this can severely impact performance, often resulting in a “waterfall” of blocked requests.

Multiplexing addresses these problems by allowing multiple request and response messages to be in flight at the same time; it’s even possible to intermingle parts of one message with another on the wire.

This, in turn, allows a client to use just one connection per origin to load a page.