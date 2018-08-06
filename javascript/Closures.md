technique for implementing lexically scoped name bindings with first class functions

from Kyle Simpson: 

> Closure is when a function "remembers" its lexical scope even when function is executed outside that lexical scope


## first class functions
Closures typically appear in languages in which functions are first-class values—in other words, such languages enable functions to be passed as arguments, returned from function calls, bound to variable names, etc., just like simpler types such as strings and integers. 

```
// Return a list of all books with at least 'threshold' copies sold.
function bestSellingBooks(threshold) {
  return bookList.filter(
      function (book) { return book.sales >= threshold; }
    );
}
```

for it to be a closure: 

1. the function needs to access lexical scope
2. it needs to be called outside their scope

> A closure—unlike a plain function—allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.