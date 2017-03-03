#### Connecting Angular http service to Web Api ###

## Web API Routing has three main phases:

1. Matching the URI to a route template.
2. Selecting a controller.
3. Selecting an action.

### Parameter Binding 

happens via **routing** (defined routes as /controller/action/{id})
via **url** - default for primitive types, but can be forced on the server with [FromUri] attribute
via **json** - default for complex types, but can be forced on the server with [FromBody] attribute.


## JSON vs url vs form encoded
These are the common methods to supply data to the server. Json could be useful when transferring complex types but not needed for primitives. When using json with complex types make sure to JSON.stringify the object.

## Examples

primitive value put

    deleteFeeRateValue(rateValueId:number){
        return this.http.put(this.config.api.deletefeeratevalue, rateValueId, this.putHeaders());
    }


    private putHeaders(){
        let headers = new Headers();
        headers.append('Content-Type', 'application/json');
        return new RequestOptions({
            headers: headers
            , withCredentials: true
        });
    }


complex type put

    addFeeRateValue(rateId:number, amountTo = null, value = null){
        var o = {PARENT_ID:rateId, AMOUNT_TO: amountTo, VALUE: value};
        return this.http.put(this.config.api.addfeeratevalue, JSON.stringify(o), this.putHeaders());
    }

Common issues
#### 400 bad request
request was malformed; invalid JSON 

'mo readin

[Parameter Binding in ASP.NET Web API](https://docs.microsoft.com/en-us/aspnet/web-api/overview/formats-and-model-binding/parameter-binding-in-aspnet-web-api)

[Routing and Action Selection in Web API](https://docs.microsoft.com/en-us/aspnet/web-api/overview/web-api-routing-and-actions/routing-and-action-selection)
