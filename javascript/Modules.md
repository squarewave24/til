### TypeScript Internal Modules
TS internal modules now renamed *Namespaces* are based on JS internal module pattern 
```
module MyInternalModule {
  export class MyClass { }
}
```
When you compile your typescript files your modules are converted into variables that nest as necessary to form namespace-like objects.<br />

```
var MyInternalModule;
(function (MyInternalModule) {
    var MyClass = (function () {
        function MyClass() {
        }
        return MyClass;
    })();
    MyInternalModule.MyClass = MyClass;
})(MyInternalModule || (MyInternalModule = {}));
var x = new MyInternalModule.MyClass();
```
class defined within the module is neatly isolated using an IIFE<br />
classes are exposed as public variables 

```
import Helpers = MyInternalModule.Helpers;
var x = new Helpers.MyClass();
```
Since TS can't import classes the way c# would, a ***shortcut*** is assigned to a local variable. 

*when you are running Typescript 1.6 or later you can replace the module syntax with the namespace syntax that is supported by the new Ecmascript 6 standard*

### TypeScript External Modules
While internal modules can be seen as namespaces for your code, external modules must be viewed as ... well modules

*External modules are meant to be loaded by a module loader. RequireJS for example is a module loader. Alternatives are System and the commonJS module loader employed by NodeJS. They all have one thing in common. A single javascript file is a module when you work with NodeJS, RequireJS or System.*

```
export class MyClass {
}
export var x:MyClass instance = new MyClass();
```
compiled with commonJS syntax: 
```
var MyClass = (function () {
    function MyClass() {
    }
    return MyClass;
})();
exports.MyClass = MyClass;
exports.x = new MyClass();
```
External modules can be imported using the `var mymodule = require('./mymodule')` syntax.

External modules will:

1. when building external modules will automatically order dependencies 
2. eliminate the need for for `///<reference path="..." />
3. eliminate the need for IIFE closures

```
// app.ts
import {module} from 'angular';

export let app = module('app',  [
        require('angular-ui-router'),
        require('angular-animate'),
        require('angular-ui-bootstrap'),
        require('angular-translate')
    ]);
```

