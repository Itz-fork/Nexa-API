# Python Nexa API
```python
from asyncio import run
from nexa_api import Nexa_API

async def main():
    client = Nexa_API()
    print(await client.fact())

run(main())
```
Asynchronous Python API wrapper for the Nexa API