## append()   prepend()

performs an insertion operation, that is, it adds nodes to the DOM tree.

Furthermore, an argument can be even a string. So, while with appendChild() a rather verbose syntax must be employed:

```
parent.appendChild(document.createTextNode('just some text'))
```


## after()  before() 

another insertion method, but this time it must be called on a child node, that is, a node with a definite parent. Nodes are inserted as adjacent siblings, as can be seen in the following example

## replaceWith()

Suppose we wanted to replace one DOM node with another. Of course, they might have children, so this operation would substitute entire DOM subtrees.

## remove()

What about removing nodes from the DOM tree? The ‘old’ method is removeChild(). As indicated by its name, it must be called on the parent of the node n to be deleted:

However, with remove(), the operation is considerably more straightforward

## insertAdjacentHTML

Before concluding, a few words about insertAdjacentHTML. It provides insertion operations similar to the first four methods listed above — append(), prepend(), after(), before() — and content to be added is specified with a string of HTML