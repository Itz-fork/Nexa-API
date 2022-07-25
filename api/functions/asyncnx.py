# Copyright (c) 2022 - Itz-fork

from functools import partial
from asyncio import get_running_loop, get_event_loop


async def run_async(func, *args, **kwargs):
    """
    Run synchronous functions in a non-blocking coroutine

    ### Arguments

        `func` : function - Function that you want to execute
    """
    try:
        loop = get_running_loop()
    except:
        loop = get_event_loop()
    return await loop.run_in_executor(
        None,
        partial(func, *args, **kwargs)
    )
