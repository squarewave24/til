### Inline caching

generic property lookup algos can be costly, therefore most VM's use a *Inline Cache*. This cache saves the path to an object for subsequent retrievals. 


    We know that it is costly to figure out where the given property is inside an arbitrary object, so we would like to do this lookup once and then put the path to this property into a cache using object’s shape as a key. Next time we see an object with the same shape we can just get the path from the cache instead of computing it from scratch.

example

    function f(o) {
    return o.x
    }

    f({ x: 1 })
    f({ x: 2 })

Given that {x: 1} and {x: 2} have the same shape (aka _hidden class_ or _map_), there is 1 cached entry here so **cache size is 1**.

this cache is **monomorphic**


    f({ x: 3, y: 1 })

    {x: 3} and {x: 3, y: 1} are objects of different shapes so the cache is no longer monomorphic, it now contains two cache entries one for a shape {x: *} and one for a shape {x: *, y: *} - our operation now is in polymorphic state with a degree of polymorphism 2.

If we continue calling f with objects of different shapes it’s degree of polymorphism will continue to grow until it reaches a predefined threshold - maximum possible capacity for the inline cache (e.g. 4 for property loads in V8) - at that point cache will transition to a megamorphic state.

    Megamorphic state exists to prevent uncontrolled growth of polymorphic caches, it means “I have seen too many shapes here, I give up tracking them”. In V8 megamorphic ICs can still continue to cache things but instead of doing it locally they will put what they want to cache into a global hashtable. This hashtable has a fixed size and entries are simply overwritten on collisions.

test

    function ff(b, o) {
    if (b) {
        return o.x
    } else {
        return o.x
    }
    }

    ff(true, { x: 1 })
    ff(false, { x: 2, y: 0 })
    ff(true, { x: 1 })
    ff(false, { x: 2, y: 0 })

1. How many property access inline caches are in the function ff?
2. What’s state they are in?

there are 2 caches, both are monomorphic because each sees only objects of one shape.

### Performance implications

* monomorphic is the fastest possible IC state if you hit the cache all the time (ONE TYPE GOOD);
* ICs in polymorphic state perform linear search among cached entries;
* ICs in megamorphic state probe global hash table and thus are slowest among ICs, but hitting global cache is still better than complete IC miss;
* IC miss is expensive - you have to pay for transitioning to runtime plus cost of the generic operation.


However this is only half of the truth: in addition to speeding up your code inline caches also serve as spies for almighty optimizing compiler — which will eventually come and try to speed your code up even further.

### Speculations and optimizations

Inline caches can’t deliver peak performance alone due to two issues:

* each IC acts on its own, knowing nothing about its neighbors;
* each IC can ultimately fallback to runtime if it can’t handle its input: which means it’s essentially a generic operation with generic side-effects and often unknown result type.

    function g(o) {
        return o.x * o.x + o.y * o.y
    }

    g({x: 0, y: 0})


[source by Vyacheslav Egorov](http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html)