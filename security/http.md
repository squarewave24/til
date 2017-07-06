[AWS conf](https://aws.amazon.com/summits/london/)

### Strict Transport Security (HSTS) [link](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet)
stops SSL downgrade and MiT attack<br />
set in response headers<br />
Once a supported browser receives this header that browser will prevent any communications from being sent over HTTP to the specified domain and will instead send all communications over HTTPS. It also prevents HTTPS click through prompts on browsers.<br />
HSTS automatically redirects HTTP requests to HTTPS for the target domain<br />
HSTS does not allow a user to override the invalid certificate message<br />

### Public Key Pinning (HPKP) [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning)
tells a web client to associate a specific cryptographic public key with a certain web server to decrease the risk of MITM attacks with forged certificates<br />
return the Public-Key-Pins HTTP header when your site is accessed over HTTPS<br />

### Content Security Policy (CSP) [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
dded layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. <br />
return the Content-Security-Policy HTTP header (sometimes you will see mentions of the X-Content-Security-Policy header,but that's an older version and you don't need to specify it anymore).<br />
Alternatively, the &lt;meta&gt; element can be used to configure a policy, for example: &lt;meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';"&gt;<br />

### Referrer-Policy [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) [link] (https://scotthelme.co.uk/a-new-security-header-referrer-policy/) 
stops client from leaking web history to third parties<br />
header governs which referrer information, sent in the Referer header, should be included with requests made.<br />

### X-Content-Type-Options [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options)
stops the clients second guessing the type of content returned by server<br />
header is a marker used by the server to indicate that the MIME types advertised in the Content-Type headers should not be changed and be followed.<br />