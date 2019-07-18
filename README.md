# Python Placeholder

Generate dynamic multi color box or dummy images, just like "Lorem Ipsum" text :D

<img src="https://raw.githubusercontent.com/salmanwaheed/python-placeholder/master/screenshot.png" width="400">

## Guidelines

```bash
# start dev server
docker-compose up

# stop dev server
docker-compose stop

curl -H Host:0.0.0.0:5000 -i http://0.0.0.0:5000
# HTTP/1.0 200 OK
# Content-Length: 2402
# Content-Type: image/png
# Cache-Control: public, max-age=43200
# Expires: Fri, 19 Jul 2019 09:46:13 GMT
# Server: Werkzeug/0.15.5 Python/3.6.5
# Date: Thu, 18 Jul 2019 21:46:13 GMT

# Warning: Binary output can mess up your terminal. Use "--output -" to tell
# Warning: curl to output it to your terminal anyway, or consider "--output
# Warning: <FILE>" to save to a file.

# e.g.http://0.0.0.0:5000/?width=500&height=500&bgcolor=white&textcolor=black
# Options:
width:
  type: int
  default: 300
height:
  type: int
  default: 200
bgcolor:
  type: str
  default: darkgrey
text:
  type: str
  default: 300x200
textcolor:
  type: str
  default: black
textsize:
  type: int
  default: 20
textalign:
  type: str
  default: center
```

## You may have some issues / errors while setup or after installation

```bash
docker ps -aq # List all containers (only IDs).
docker stop $(docker ps -aq) #Stop all running containers
docker rm $(docker ps -aq) # Remove all containers.
docker rmi $(docker images -q) # Remove all images.

# If you get >>> OSError: [Errno 48] Address already in use
ps -fA | grep python3 # try to find out PID

kill -9 YOUR-PID # lets kill PID
```

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
