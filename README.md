# Nexa-APIs 🌊

Simple API made with [Fastapi](https://fastapi.tiangolo.com/) that relys on other APIs to fetch data (**wtf?**)


# List of endpoints 🎗️

- [`reddit`](api/routes/reddit.py) - Search for posts in reddit
- [`urban dict`](api/routes/urbandict.py) - Search for definitions in urban dict
- [`wallpapers`](api/routes/wallpapers.py) - Fetch wallpapers from reddit
- [`translate`](api/routes/translate.py) - Translate text using google translate


# Deploy it! 🪐

### Locally 💻,
```sh
git clone https://github.com/Itz-fork/Nexa-APIs
cd Nexa-APIs
pip3 install -r requirements.txt
uvicorn api.main:app
```

### Heroku ☁️
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Itz-fork/Nexa-APIs)


# Development 🧑‍💻

Here are somethings to note,

- You can find config files in [`config`](api/config) directory
- Reusable functions are located in [`functions`](api/functions) directory
- You can find routes in [`routes`](api/routes) directory
- Use [`start script`](start.sh) when running the dev server

## Add new routes 👨‍🎨
- Create a new file in [`routes`](api/routes) directory (Ex: `myRoute.py`)
- Add this code (Here we add new route named `/test` which returns the text, `Hello from Fastapi, Nexa-APIs 🌊`)
```python
from fastapi import APIRouter
from functions.response import send_response

route = APIRouter()

@route.get("/test")
async def test_route():
    return await send_response("Hello from Fastapi, Nexa-APIs 🌊")
```
- Run the API
```sh
bash start.sh
```


# Why? 🤔

> __**Cuz why not? 🎾**__


# License & Credits 👮‍♂️ ♥️

- Licensed under [MIT License](LICENSE)
- Credits to [emoji - aranja](https://emoji.aranja.com/) for the [favicon](favicon.ico)