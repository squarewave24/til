### Change Detection ###
disable global, trigger as needed

    constructor(private cd: ChangeDetectorRef);
    ...
       Observable.from(...).subscribe(o => {
           this.o = o;
           this.cd.detectChanges()
           })


### Async Pipe ###  
bind to asynchronous primitive. <br />
automatic value unwrapping. <br />
automatic unsubscription from observable when dom element is removed.

### Change Detection 

happens via Zones. All js code within ng runs in Zones which wrap native code in wrappers. this makes it possible to expose hooks around all events. 

    Zone > fork > ngZone

^^^ zones are forked and there is a ng2 fork. 

    this.zone.onTurnDone
       .subscribe(() => this.zone.run(()=> this.tick;))

    tick() {
        this.changeDetectorRefs
            .forEach((ref) => ref.detectChanges())
    }

**Each change detector is not a single class in angular that dynamically runs change detection for every component. Angular generates classes for you at runtime which are specificially written for your component. This makes it fast becasue it's [monomorphic](monomorphism.md). When you have a change detector that knows about shape of all javascript objects. this particular shape doesn't change. VM's can optimize that code since it's monomorphic they can inline this code.

* Change Detection Graph is a directed tree
* way more predictable
* gets stable after a single pass
* generates VM friendly code for better performance

## Immutables + On Push

Angualr can skip a lot of deep checks if objects are immutable. We can assume that if object ref has not changed, nothing within that object changed. 

OnPush will **tell Angular to skip change detection** for a component subtree if none of its inputs changed

    @Component({
    // ...
    changeDetection: ChangeDetectionStrategy.OnPush
    })

#### Observables

Unlike immutable objects they don't give us new references when a change is  made. Instead of they fire events we use to fire changes. 

    constructor(private cd: ChangeDetectorRef) {}
    ngOnInit() {
        this.addItemStream.subscribe(() => {
        this.counter++; // application state changed
        this.cd.markForCheck(); // marks path
        })
    }
    }

[Demos](https://github.com/thoughtram/angular2-change-detection-demos)

[Pascal Precht blog post](https://blog.thoughtram.io/angular/2016/02/22/angular-2-change-detection-explained.html)
[ng-nl 2016 talk by Pascal Precht](https://www.youtube.com/watch?v=CUxD91DWkGM)