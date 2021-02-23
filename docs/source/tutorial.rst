Tutorial
========

This guide can help you start working with tinHTTPie.

Header of a GET Request
-----------------------

Make a GET request and return only the header of the response by adding the ``-H`` flag::

    $ tihttp -H google.com

You will see the header of the response which looks like::

    Cache-Control: private, max-age=0
    Content-Encoding: gzip
    Content-Length: 5632
    Content-Type: text/html; charset=ISO-8859-1
    Date: Tue, 23 Feb 2021 17:43:53 GMT
    ...

Body of a GET Request
---------------------


Or use the ``-B`` flag to print only the body::

    $ tihttp -B http://jsonplaceholder.typicode.com/todos?id=1

It will look like this::

    [
      {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
      }
    ]
