# fastfast
messing with fastapi+fasthtmx

Run the app with

```sh
make run
```

If you go to http://localhost:8000 you should see a page formatted with html.

Or you can ping it as an API with:

```sh
$ http http://localhost:8000/ 'Accept:application/json'

HTTP/1.1 200 OK
content-length: 33
content-type: application/json
date: Sat, 07 Sep 2024 00:14:16 GMT
server: uvicorn

{
    "colors": [
        "red",
        "green",
        "blue"
    ]
}
```
