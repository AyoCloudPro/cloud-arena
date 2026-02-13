from datetime import datetime, timezone

from app.config import settings

import socket
import psutil

def get_system_info():
    # CPU Usage
    cpu_percent = psutil.cpu_percent(interval=None)

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_used_mb = round(memory.used / (1024 * 1024), 2)
    memory_percent = memory.percent

    # Container ID in Docker
    hostname = socket.gethostname()

    #Uptime
    uptime_seconds = (datetime.now(timezone.utc) - settings.START_TIME).total_seconds()

    return {
        "hostname": hostname,
        "cpu_usage_percent": cpu_percent,
        "memory_used_mb": memory_used_mb,
        "memory_usage_percent": memory_percent,
        "uptime_seconds": uptime_seconds
    }

system_info = get_system_info()
