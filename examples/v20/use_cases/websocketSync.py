import random
import asyncio
from examples.v20.use_cases.mainCsms import main as csmswebsocket
from examples.v20.use_cases.mainCp import conn as cpwebsocket , func as getData

async def sync_client_server_websocket(csms , cp):
    m=random.randint(2001,9999)
    await asyncio.gather(csmswebsocket(csms,m))
    await asyncio.gather(cpwebsocket(cp,m))
    return getData()

    


