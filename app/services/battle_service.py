from app.config import settings
from app.services.system_info import system_info

import random
import asyncio


async def simulate_cloud_response(cloud_name: str, min_delay=50, max_delay=250):
    """
    Simulates latency difference between clouds.
    """
    delays_ms = random.randint(min_delay, max_delay)
    await asyncio.sleep(delays_ms / 100)

    return {
        "cloud": cloud_name,
        "region": settings.REGION,
        "latency_ms": delays_ms,
        "memory_usage_percent": system_info["memory_usage_percent"],
        "cpu_usage_percent": system_info["cpu_usage_percent"]
    }