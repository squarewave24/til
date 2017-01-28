# scope 

scope is invoked when LHS or RHS lookup is performed. 

    a = 2; 

left hand side lookup (target of assignment) will check local scope, and then go up the tree of **nested scopes** until we reach global scope. 

    var q = x;

same thing happens by RHS (source of assignemnt)

*in the case of variable not being declared, RHS will throw undefined exception while LHS will simply declare it on global scope*

# lexical scope

*exical scope is scope that is defined at lexing time. In other words, lexical scope is based on where variables and blocks of scope are authored, by you, at write time, and thus is (mostly) set in stone by the time the lexer processes your code*

global variables can be "shadowed" when the same var is declared down the stack of scopes. 

global variables can still be accessed via window.x 

shadowed variables in other scopes can not be accessed. 

*No matter where a function is invoked from, or even how it is invoked, its lexical scope is only defined by where the function was declared*

