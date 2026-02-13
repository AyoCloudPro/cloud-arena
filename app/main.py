from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timezone

from app.config import settings
from app.services.system_info import system_info
from app.services.battle_service import simulate_cloud_response

import time
import os

app = FastAPI()

current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)


# Health Check
# ==================
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# Index route
# =======================
@app.get("/")
async def root(request: Request):
    uptime_seconds = (datetime.now(timezone.utc) - settings.START_TIME).total_seconds()
        
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
            "cloud_provider": settings.CLOUD_PROVIDER,
            "region": settings.REGION,
            "version": settings.VERSION,
            "build_number": settings.BUILD_NUMBER,
            "uptime_seconds": uptime_seconds,
            **system_info
        }
    )


@app.get("/api/stats")
async def get_stats():
    start = time.perf_counter()

    response_time_ms = round((time.perf_counter() - start) * 1000)

    return JSONResponse(
        content={
            "cloud": settings.CLOUD_PROVIDER,
            "responseTime": f"{response_time_ms}ms",
            "region": settings.REGION,
            "memoryUsage": round(system_info["memory_usage_percent"]),
            "cpuUsage": round(system_info["cpu_usage_percent"]),
            "dockerImage": settings.DOCKER_IMAGE,
            "environment": settings.ENVIRONMENT,
            "buildNumber": settings.BUILD_NUMBER,
        }
    )


@app.get("/api/cloud1")
async def cloud1():
    return await simulate_cloud_response("AWS")


@app.get("/api/cloud2")
async def cloud2():
    return await simulate_cloud_response("GCP")