O terceiro dia do bloco trata de conceitos relacionados à internet de forma
geral. Entre eles: Cliente, Servidor, Endereço IP, TCP/IP, ISP, DNS,
Port Number, Host, HTTP e URL. Além disso, vimos os métodos de requisições GET,
POST, PUT e DELETE.

Enquanto o dia não teve uma lista de exercícios sugeridos, eu acho os exercícios
do link a seguir, propostos por Julia Evans, bem apropriados como exercícios de
fixação:

[21 curl exercises](https://jvns.ca/blog/2019/08/27/curl-exercises/)

1. Request https://httpbin.org
2. Request https://httpbin.org/anything. httpbin.org/anything will look at the request you made, parse it, and echo back to you what you requested. curl’s default is to make a GET request.
3. Make a POST request to https://httpbin.org/anything
4. Make a GET request to https://httpbin.org/anything, but this time add some query parameters (set `value=panda`).
5. Request google’s robots.txt file (www.google.com/robots.txt)
6. Make a GET request to https://httpbin.org/anything and set the header `User-Agent: elephant`.
7. Make a DELETE request to https://httpbin.org/anything
8. Request https://httpbin.org/anything and also get the response headers
9. Make a POST request to https://httpbin.org/anything with the JSON body `{"value": "panda"}`
10. Make the same POST request as the previous exercise, but set the Content-Type header to `application/json` (because POST requests need to have a content type that matches their body). Look at the `json` field in the response to see the difference from the previous one.
11. Make a GET request to https://httpbin.org/anything and set the header `Accept-Encoding: gzip` (what happens? why?)
12. Put a bunch of a JSON in a file and then make a POST request to https://httpbin.org/anything with the JSON in that file as the body
13. Make a request to https://httpbin.org/image and set the header ‘Accept: image/png’. Save the output to a PNG file and open the file in an image viewer. Try the same thing with different `Accept:` headers.
14. Make a PUT request to https://httpbin.org/anything
15. Request https://httpbin.org/image/jpeg, save it to a file, and open that file in your image editor.
16. Request https://www.twitter.com. You’ll get an empty response. Get curl to show you the response headers too, and try to figure out why the response was empty.
17. Make any request to https://httpbin.org/anything and just set some nonsense headers (like `panda: elephant`)
18. Request https://httpbin.org/status/404 and https://httpbin.org/status/200. Request them again and get curl to show the response headers.
19. Request https://httpbin.org/anything and set a username and password (with `-u username:password`)
20. Download the Twitter homepage (https://twitter.com) in Spanish by setting the `Accept-Language: es-ES` header.
21. Make a request to the Stripe API with curl. (see https://stripe.com/docs/development for how, they give you a test API key). Try making exactly the same request to https://httpbin.org/anything.
