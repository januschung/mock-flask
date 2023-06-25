#### Introduction

This is a simple REST mock server written with Python `3.11` and Flask `2.3.2`. It also comes with Gunicorn which enables hot reload for local development.

It provides sample endpoints to render output either based on static resource file or simple logic as defined in `mock.py`.

The server can either be brought up as a standalone python application or as a docker.

Feel free to provide feedback or feature request.


#### Customize the Mock Service

Every logic is definied in `mock.py`. You can modify the return value for `/resource` endpoint by editing the file under `static` folder.


#### Available Endpoints:


<details>
<summary>/resource?data=[value]</summary>

This mock service returns static response from the file located in `src/main/resources/data`


_Sample 1_

**curl "http://localhost:5000/resource?data=100"**


will return 

```console
[
 {"id":"100","name":"jack","age":"30"},
 {"id":"101","name":"jill","age":"32"}
]
```

_Sample 2_

**curl "http://localhost:5000/resource?data=200"**


will return

```console
[
 {"id":"200","name":"tom","age":"40"},
 {"id":"201","name":"jerry","age":"28"}
]
```

When request with a non existing file, the response will be reading from file `empty`

_Sample 3_

**curl "http://localhost:5000/resource?data=300"**


will return

```console
[]
```
</details>

<details>
<summary>/status?code=[value]</summary>

_Sample 1_


**curl "http://localhost:5000/status?code=200"**


will return status code 200 and the following response

```console
200 OK
```

_Sample 2_

**curl "http://localhost:5000/status?code=400"**


will return status code 400 and the following response

```console
400 BAD_REQUEST
```

</details>

<details>
<summary>/delay?code=[value]</summary>

_Sample 1_


**curl "http://localhost:5000/delay?ms=3000"**


will return response with 3000 milliseconds delay

```console
Response with delay of 3000 milliseconds
```
</details>

#### Build and run
```console
gunicorn --reload --bind localhost:3000 "app:create_app"
```
#### Build and run with docker-compose
```console
docker-compose up -d
```

## Contributing
I appreciate all suggestions or PRs which will help making the mock better. Feel free to fork the project and create a pull request with your idea.

#### To do
1. Add Openapi