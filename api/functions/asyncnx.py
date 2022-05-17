# Copyright (c) 2022 Itz-fork

from functools import partial
from asyncio import AbstractEventLoop, get_running_loop


async def run_async(func, *args, loop: AbstractEventLoop = None, exec=None):
    """
    ## Huh?
    Run synchronous functions in a non-blocking coroutine

    ## Arguments

        Required:

            `func` (type: function) - Function that you want to execute
            `*args` (type: Any) - Arguments

        Optional:

            `loop` (type: AbstractEventLoop) - An event loop
            `exec` (type: Any) - Executor

    """
    if not loop:
        loop = get_running_loop()
    return await loop.run_in_executor(
        exec,
        partial(func, args)
    )
