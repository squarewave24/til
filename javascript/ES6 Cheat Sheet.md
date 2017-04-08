## let vs var ##

let = block scope. enforces a stylistic pattern of local scoping within a function.
let also creates a new instance in each iteration of a for loop

var = variable to be used within entire scope of a X (function, window etc)

## const ## 
assignment that cannot be re-assigned. 

not immutable. to make it immutble you could use `object.freeze(x)`. 

const value can't be freed up for garbage collection by setting it to null

## default values ## 

```
x = x || 42; // 0 is falsy and it will still fall through 42
x = x !== undefined ? x : 42; // more explicit 
function foo(x = 42) // works across all scenarios (null,undefined,empty array)
```

## lazy expression ## 

``` 
function foo(x = bar()) // gets called only if used
function foo(x = uniqueId()) // possible use
function foo(x = throwIfempty()) // enforce 
```

## rest & spread ##
gather (rest) works on anything that iterable

```
var args = [].slice.call( arguments ); // old school way to get an array out of arguments
function foo(...args1) { //  gathers 
    bar (42, ...args1)   //  spreads 42, x,y,z
}
```
random thought: purpose of abstraction is focus. hyper focus on specific functionality
```
var z = [0].concat(x,y,[6]); // imperative
var z = [0,...x,...y,6];     // declarative

var a = [2,3,4];
var b = [ 1, ...a, 5 ]; // used in another variable

...'hello' // string becomes an array of chars
```

## array destructuring ## 
assigning individual parts of a structure (object/function) into separate units. 
```
var [a,b,c] = [0,1,2,3,4,5]; // assign first 3 values to individual variables

white space and new lines are free and great for code readibility

```javascript

var [
    a,
    b = 42, // default
    obj.c,  // assign to another object
    [
        c, // destrcure nested array
        d,
    ],
    ...args // gather the rest of them 
] 

[x,y] = [y,x] // reassign  order
[,,a,b,c] // discard first 2 items
```