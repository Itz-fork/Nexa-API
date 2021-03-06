<h1 align="center">
    Nexa API ๐ <br/>
    <img src="https://user-images.githubusercontent.com/77770753/173895688-fc1d19e7-bbb1-446f-a3b5-4f417e6f3fc4.png" width="200">
</h1>

<p align="center">
    <b>Simple</b>, <b>Free</b> and <b>Easy to use</b> Public api </br></br>
    <kbd>โ<br>โ<a href="#list-of-endpoints-%EF%B8%8F">Endpoints</a>โ<br>โ</kbd>
    <kbd>โ<br>โ<a href="#deploy-it-">Deployment</a>โ<br>โ</kbd>
    <kbd>โ<br>โ<a href="#development-">Development</a>โ<br>โ</kbd>
</p>



# List of endpoints ๐๏ธ
- Search
    - [`reddit`](api/routes/reddit.py) - Search for posts in reddit
    - [`urban dict`](api/routes/urbandict.py) - Search for definitions in urban dict
    - [`wallpapers`](api/routes/wallpapers.py) - Fetch wallpapers from reddit
    - [`npm search`](api/routes/npm_search.py) - Search for npm packages
    - [`1337x search`](api/routes/1337x_search.py) - Search for torrents in 1337x

- Language
    - [`acronym`](api/routes/acronyms.py) - Get the meaning of an acronym
    - [`define`](api/routes/define.py) - Get the definition of a word
    - [`translate`](api/routes/translate.py) - Translate text using google translate

- Tools
    - [`password`](api/routes/password.py) - Generates a random password according to the given length
    - [`color_palette`](api/routes/color_palette.py) - Generate color palettes from images
    - [`currency`](api/routes/currency_cov.py) - Exchange rate from 'x' to 'y'. Data is **scraped** from [x-rates](https://www.x-rates.com/)

- File server
    - [`storage`](api/routes/storage.py) - Store files on the server [Read more](https://github.com/Itz-fork/Nexa-API/wiki/Route:-Storage)

- Fun
    - [`fact`](api/routes/facts.py) - Get a random fact
    - [`insult`](api/routes/insult.py) - Insult somebody ( โงโ อสโ)


# Deploy it! ๐
This api is open source, you can deploy your own version easily ๐ค

### Locally ๐ป,
```sh
git clone https://github.com/Itz-fork/Nexa-API
cd Nexa-API
pip3 install -r requirements.txt
bash start.sh
```

### Heroku โ๏ธ
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Itz-fork/Nexa-API)


# Development ๐งโ๐ป
Here are somethings to note,

- You can find config files in [`config`](api/config) directory
- Reusable functions are located in [`functions`](api/functions) directory
- You can find routes in [`routes`](api/routes) directory
- Use [`start script`](start.sh) when running the dev server (`bash start.sh dev`)

## Add new routes ๐จโ๐จ
- Create a new file in [`routes`](api/routes) directory (Ex: `myRoute.py`)
- Add this code (Here we add new route named `/test` which returns the text, `Hello from Fastapi, Nexa API ๐`)
```python
from fastapi import APIRouter
from ..functions.response import send_response

route = APIRouter()

@route.get("/test")
async def test_route():
    return await send_response("Hello from Nexa API ๐")
```
- Start the development server
```sh
bash start.sh dev
```


# License & Credits ๐ฎโโ๏ธ โฅ๏ธ
- Licensed under [MIT License](LICENSE)
- Color scheme by [catppuccin](https://github.com/catppuccin/catppuccin)
- Swagger UI Dark theme by [Itz-fork](https://github.com/Itz-fork/Fastapi-Swagger-UI-Dark)
