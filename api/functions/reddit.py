# Copyright (c) 2022 - Itz-fork

from re import search
from .http_req import fetch


async def add(req, arr: list):
    no = 1
    for chl in req["data"]["children"]:
        try:
            p_data = {}
            p_data["result_no"] = no
            p_data["subreddit"] = chl["data"]["subreddit_name_prefixed"]
            p_data["title"] = chl["data"]["title"]
            p_data["author"] = chl["data"]["author"]
            p_data["post_link"] = "https://www.reddit.com{}".format(
                chl["data"]["permalink"])
            if search(r'\bredd.it\b', chl["data"]["url"]):
                p_data["image"] = chl["data"]["url"]
            else:
                p_data["image"] = ""
            p_data["post_content"] = chl["data"]["selftext"]
            arr.append(p_data)
            no += 1
        except:
            pass


async def request(q: str, subs: list = [], nsfw: bool = False):
    data = []
    nprm = "&restrict_sr=true&include_over_18=on" if nsfw else ""
    if subs:
        for s in subs:
            resp = await fetch(f"https://www.reddit.com/r/{s}/search.json?q={q}{nprm}")
            await add(resp, data)
    else:
        resp = await fetch(f"https://www.reddit.com/search.json?q={q}{nprm}")
        await add(resp, data)
    return data
