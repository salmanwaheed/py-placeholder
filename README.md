# Python Placeholder

Generate dynamic multi color box or dummy images, just like "Lorem Ipsum" text :D

<img src="https://raw.githubusercontent.com/salmanwaheed/python-placeholder/master/screenshot.png" width="400">

## Guidelines

```bash
pip3 install -r requirements.txt

# use below command for local deployment
python3 -m flask run # open your browser at http://127.0.0.1:5000/

# e.g. http://127.0.0.1:5000/?width=500&height=500&bgcolor=white&textcolor=black
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
# If you get >>> OSError: [Errno 48] Address already in use
ps -fA | grep python3 # try to find out PID

kill -9 YOUR-PID # lets kill PID
```

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
