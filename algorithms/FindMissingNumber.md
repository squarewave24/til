An efficient way to find a missing number 

given multiple arryas with 1 missing number have a few options to find a missing value

1. sort both arrays, loop over them to find the missing number

    this has a problem of additional space/time complexity of the sort in addition to the O(n) search time. 

2. add/subtract both arrays. 

    this will add log n space complexity in order to store the sum 

3. fastest way to do this is to XOR both arrays and then XOR the results which will provide the missing number. On time 1n space (i think!)

```
var a1 = [2,5,8,12,36];
var a2 = [2,8,12,5];

function findMissing(a1, a2) {
  var res = 0;
  a1.forEach(a1n => res = res ^ a1n);
  a2.forEach(a2n => res = res ^ a2n);
  return res;
}

console.log('result: ', findMissing(a1, a2));

```