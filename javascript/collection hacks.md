### iterate empty array

   ````
   let arr = new Array(4); // [undefined,undefined,undefined,undefined]
   ````

   ````
   let arr = new Array(4);
   arr.map((elem,index)) => index); // [undefined,undefined,undefined,undefined]
   ````

   ````
   // use apply
   let arr = Array.apply(null, new Array(4))
   arr.map((elem, index) => index); // [0, 1, 2, 3]
   ````

  ````
  // using spread
  arr = [...new Array(4)];
  arr.map((elem, index) => index); // [0, 1, 2, 3]
  ````


### Unique array

````
// using spread
let arr = [...new Set([1,2,3,3])]; // [1, 2, 3]
````


### Get End Elements 
````
[1,2,3,4,5,6].slice(-2); // [5,6]
````