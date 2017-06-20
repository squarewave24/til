## Map
scrubbing values into something / transforming values. 

don't write any side effect code here

## ForEach
subscribes to observable<br />
similar to subscribe <br />
non cancellable way to call observable<br />
for side effects <br />

## Do
*Invokes an action for each element in the observable sequence and invokes an action upon graceful or exceptional termination of the observable sequence.*

*Returns (Observable): The source sequence with the side-effecting behavior applied.*

**try to keep your side effect code here**

## Subscribe

side effects