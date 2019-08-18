The TC39 async iterators proposal that brought for/await/of to JavaScript also introduced the concept of an async generator function. Now, JavaScript has 6 distinct types of functions:

Normal functions `function() {}`
Arrow functions `() => {}`
Async functions `async function() {}`
Async arrow functions `async () => {}`
Generator functions `function*() {}`
Async generator functions `async function*() {}`


practical usecase for  async generator

```
'use strict';

const mongoose = require('mongoose');

async function* run() {
  await mongoose.connect('mongodb://localhost:27017/test', { useNewUrlParser: true });
  await mongoose.connection.dropDatabase();

  const Model = mongoose.model('Test', mongoose.Schema({ name: String }));
  for (let i = 0; i < 5; ++i) {
    await Model.create({ name: `doc ${i}` });
  }

  // Suppose you have a lot of documents and you want to report when you process
  // each one. You can `yield` after processing each individual doc.
  const total = 5;
  const cursor = Model.find().cursor();

  let processed = 0;
  for await (const doc of cursor) {
    // You can think of `yield` as reporting "I'm done with one unit of work"
    yield { processed: ++processed, total };
  }
}

(async () => {
  for await (const val of run()) {
    // Prints "1 / 5", "2 / 5", "3 / 5", etc.
    console.log(`${val.processed} / ${val.total}`);
  }
})();
```

http://thecodebarbarian.com/async-generator-functions-in-javascript.html