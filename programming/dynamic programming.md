## Dynamic programming

amounts to breaking down an optimization problem into simpler sub-problems, and storing the solution to each sub-problem so that each sub-problem is only solved once.

### Sub-problems 
are smaller versions of original problem, build on each other to obtain a solution to origianl problem

* after you solve each sub-problem, you must memoize, or store it

let's take a recursive soltion: 

```
def fibonacciVal(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacciVal(n-1) + fibonacciVal(n-2)
```

This algorithm accomplishes its purpose, but at a huge cost. For example, let’s look at what this algorithm must calculate in order to solve for n = 5 (abbreviated as F(5)):

```
F(5)  
                    /      \                  
                   /        \
                  /          \
               F(4)          F(3)
            /       \        /   \
          F(3)     F(2)     F(2)  F(1)
         /   \     /  \     /   \
       F(2) F(1) F(1) F(0) F(1) F(0)
       /  \
     F(1) F(0)
```


 sup-problem for n=2 is solved thrice !     

 instead, let's store the n(2) and access it each time it i needed

 ```
    def fibonacciVal(n):
    memo = [0] * (n+1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
```

#### the array memo[] is memoized iteratively (n=2 calculated before n=3)

## Dynamic Programming Process

1. identity sub-problem in words
    * The maximum value schedule for punchcards n-1 through n such that the punchcards are sorted by start time
2. Write out the sub-problem as a recurring mathematical decision.
    * If my algorithm is at step i, what information would it need to decide what to do in step i+1? (And sometimes: If my algorithm is at step i, what information did it need to decide what to do in step i-1?)
3. Solve the original problem using Steps 1 and 2.
4. Determine the dimensions of the memoization array and the direction in which it should be filled.



ref: https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296