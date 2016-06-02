[function* returns a generator object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) which can be exited and re-entered. 

<strong> great way to control flow between functions.</strong> Javascript is single threaded so functions gneerally need to run to completion before program can continue but with generators they can be interrupted and flow can be redirected to external sources to be resumed later. 

<i>ES6 generator functions are "cooperative" in their concurrency behavior. Inside the generator function body, you use the new yield keyword to pause the function from inside itself. Nothing can pause a generator from the outside; it pauses itself when it comes across a yield.</i> [link](https://davidwalsh.name/es6-generators)


```javascript
function* counter() {
    var x=0;
    while (x<3){ 
        yield ++x; 
    }
}
// example 1
var c = counter();
var o = c.next();
while(!o.done){
    console.log('obj: ', o);
    if (o.done)
        console.log('finished');
    else 
        o = c.next();
};

// example 2
for (var o2 of counter()){
    console.log('value: ', o2);
}
```

This is pretty much the iterator pattern from c#. calling .next() will resume original function and return the value (Undefined if genertor function is complete). in ES6 a foreach loops is impleneted using a for..of notation. 

###Exception Handling
use regular try..catch on asynchronous calls

 






