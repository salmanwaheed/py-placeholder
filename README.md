# py-placeholder

Generate dynamic multi color box or dummy images, just like "Lorem Ipsum" text :D

<img src="https://raw.githubusercontent.com/salmanwaheed/python-placeholder/master/screenshot.png" width="400">

## Local Development

```bash
docker-compose up/down # to start or remove the server

# e.g. http://0.0.0.0:5000/?width=500&height=400&bgcolor=white&textcolor=black
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
# textalign=center
# textalign=bottom,left
# textalign=bottom,right
# textalign=top,left
# textalign=top,right
```

## License
The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
