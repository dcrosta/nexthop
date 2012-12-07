# nexthop

`nexthop` is a web application whose sole purpose is to perform HTTP
redirects using 3xx status codes.

To use nexthop, make a request to it using a URL like

    http://nexthop.cc/[code]/[next-hop-url]

And your browser will be redirected to the next hop URL.

The `[code]` may be any of

* 301
* 302
* 303
* 307

The `[next-hop-url]` may be an encoded or unencoded URL, and may contain a
query string.
