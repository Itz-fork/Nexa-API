from fastapi import APIRouter
from bs4 import BeautifulSoup

from ..functions.http_req import fetch
from ..functions.asyncnx import run_async
from ..functions.response import send_response
from ..models.Tools import CurrencyModel

route = APIRouter()


def scrape_it(resp):
    soup = BeautifulSoup(resp[0].text, "html.parser")
    rs = soup.find("span", attrs={"class": "ccOutputRslt"})
    return rs.text


@route.get(
    "/currency",
    description="Exchange rate from 'x' to 'y'. Data is **scraped** from [x-rates](https://www.x-rates.com/)",
    response_model=CurrencyModel,
    tags=["Tools"])
async def currency_converter(origin: str, to: str, amount: int | float):
    r = await fetch(f"https://www.x-rates.com/calculator/?from={origin.upper()}&to={to.upper()}&amount={amount}", False)
    s = await run_async(scrape_it, r)
    print(s)
    return await send_response(s)
