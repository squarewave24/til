# Trie 

also known as digital tree or radix tree or prefix tree, is a type of search tree. ordered tree that can store a dynamic set of associative array where keys are usually strings. 

Unlike a binary search tree, no node stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All descendants of that node have a common prefix of the string associated with that node (root has empty string). values tend to only be associated with leaf nodes and with some inner nodes that correspond to keys of interest. 

advantages over hash table:


* Looking up data in a trie is faster in the worst case, O(m) time (where m is the length of a search string), compared to an imperfect hash table. An imperfect hash table can have key collisions. A key collision is the hash function mapping of different keys to the same position in a hash table. The worst-case lookup speed in an imperfect hash table is O(N) time, but far more typically is O(1), with O(m) time spent evaluating the hash.
* There are no collisions of different keys in a trie.
* Buckets in a trie, which are analogous to hash table buckets that store key collisions, are necessary only if a single key is associated with more than one value.
* There is no need to provide a hash function or to change hash functions as more keys are added to a trie.
* A trie can provide an alphabetical ordering of the entries by key.

drawbacks:


* Tries can be slower in some cases than hash tables for looking up data, especially if the data is directly accessed on a hard disk drive or some other secondary storage device where the random-access time is high compared to main memory.[7]
* Some keys, such as floating point numbers, can lead to long chains and prefixes that are not particularly meaningful. Nevertheless, a bitwise trie can handle standard IEEE single and double format floating point numbers.
* Some tries can require more space than a hash table, as memory may be allocated for each character in the search string, rather than a single chunk of memory for the whole entry, as in most hash tables.

A common application of a trie is storing a predictive text or autocomplete dictionary, such as found on a mobile telephone. 

Tries are also well suited for implementing approximate matching algorithms,[8] including those used in spell checking and hyphenation[4] software.

<br />

![example tree](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Patricia_trie.svg/660px-Patricia_trie.svg.png)