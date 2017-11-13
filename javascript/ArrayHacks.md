
```javascript
    // Grab unique
    [1,1,2,3,4].filter( ( item, index, array ) => array.indexOf( item ) === index )
    // => [1,2,3,4] 

    // Flatten
    [[1,2],[3,4]].reduce( ( result, item ) => result.concat(item), [] );
    // => [1,2,3,4]

    // Sort
    [1,2,4,3].sort( ( a, b ) => a - b )

```
