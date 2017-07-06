In cryptography, a zero-knowledge proof or zero-knowledge protocol is a method by which one party (the prover) can prove to another party (the verifier) that a given statement is true, without conveying any information apart from the fact that the statement is indeed true.

...

The notion of 'zero knowledge' was first proposed in the 1980s by MIT researchers Shafi Goldwasser, Silvio Micali and Charles Rackoff. These researchers were working on problems related to interactive proof systems, theoretical systems where a first party (called a 'Prover') exchanges messages with a second party ('Verifier') to convince the Verifier that some mathematical statement is true.*

...

imagine that a real-world client wishes to log into a web server using a password. The standard 'real world' approach to this problem involves storing a hashed version of the password on the server. The login can thus be viewed as a sort of 'proof' that a given password hash is the output of a hash function on some password -- and more to the point, that the client actually knows the password.

...

What Goldwasser, Micali and Rackoff proposed was a new hope for conducting such proofs. If fully realized, zero knowledge proofs would allow us to prove statements like the one above, while provably revealing no information beyond the single bit of information corresponding to 'this statement is true'.



http://blog.cryptographyengineering.com/2014/11/zero-knowledge-proofs-illustrated-primer.html