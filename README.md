# helloflask
hello-world flask skeleton

## install \& run
```sh
sudo pip3 install netifaces
sudo apt-get install python3-flask
```

```sh
python3 hello.py eth0 5555
```

## test

```sh
$ curl -d '' -H "Content-Type: application/json" -X POST http://192.168.3.195:5555/somepath | python -m json.tool 
```

```sh
{
    "results": {
        "status": "fail"
    }
}
```

```sh
$ curl -d '{"x":"y"}' -H "Content-Type: application/json" -X POST http://192.168.3.195:5555/somepath | python -m json.tool
```

```sh
{
    "results": {
        "input": {
            "x": "y"
        },
        "status": "succ"
    }
}
```

