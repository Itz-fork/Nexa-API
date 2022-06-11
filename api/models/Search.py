from pydantic import BaseModel


# Route: /ud
class UrbanDictModel(BaseModel):
    q: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": [
                        {
                            "definition": "A really awesome, nice and smart boy who loves [programming].. Bruh_0x have [answers] to everything no matter what is [the question] is. That's why everybody loves him.",
                            "example": "Girl 1: Yo, [you know who] [tf] is that boy?\r\nGirl 2: Hell yeah! He is a Bruh_0x\r\nGirl 1: [uWu]!",
                            "sounds": [],
                            "author": "SomeRandomBoy",
                            "link": "http://bruh0x.urbanup.com/16875758",
                            "added_on": "2021-12-30T21:52:51.094Z",
                            "likes": 3,
                            "dislikes": 0
                        }
                    ]
                }
            ]
        }


# Route: /wallpaper
class WallpaperModel(BaseModel):
    q: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": [
                        "https://i.redd.it/8wsbd1ow7cv81.jpg",
                        "https://i.redd.it/flwo0mo5eck71.png",
                        "https://i.redd.it/sa6dompay1k51.jpg",
                        "https://i.redd.it/6w3tjwqlkg261.jpg"
                    ]
                }
            ]
        }


# Route: /reddit
class RedditModel(BaseModel):
    q: str
    sub: str = None

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": [
                        {
                            "result_no": 1,
                            "subreddit": "r/unixporn",
                            "title": "[Hyprland] Garden Revisited",
                            "author": "taylor85345",
                            "post_link": "https://www.reddit.com/r/unixporn/comments/uz3x5a/hyprland_garden_revisited/",
                            "image": "https://v.redd.it/d51is4ip42291",
                            "post_content": ""
                        }
                    ]
                }
            ]
        }


# Route: /npm
class NpmModel(BaseModel):
    q: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": [
                        {
                            "name": "svelte-daisyui",
                            "version": "0.0.1",
                            "author": "",
                            "date": "2021-12-11T03:51:58.441Z",
                            "about": "Svelte Components for [DaisyUI](https://daisyui.com)",
                            "links": {
                                "npm": "https://www.npmjs.com/package/svelte-daisyui"
                            },
                            "keywords": "",
                            "publisher": {
                                "username": "bestguy",
                                "email": "7zark7@gmail.com"
                            },
                            "maintainers": [
                                {
                                    "username": "bestguy",
                                    "email": "7zark7@gmail.com"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


# Route: /1337x
class X1337Model(BaseModel):
    q: str

    class Config:
        schema_extra = {
            'examples': [
                {
                    "status": "ok",
                    "data": {
                        "1": {
                            "name": "Red Dead Redemption 2 (Build 1311.23, MULTi13) [FitGirl Repack]",
                            "torrentId": "4651924",
                            "link": "https://www.1377x.to/torrent/4651924/Red-Dead-Redemption-2-Build-1311-23-MULTi13-FitGirl-Repack/",
                            "seeders": "4034",
                            "leechers": "8722",
                            "size": "66.3 GB",
                            "time": "Oct. 23rd '20",
                            "uploader": "FitGirl",
                            "uploaderLink": "https://www.1377x.to/FitGirl/"
                        }
                    }
                }
            ]
        }
