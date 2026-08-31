import os
from fastapi import FastAPI

app = FastAPI(
    title="Disk Usage",
    description="Simple host filesystem usage endpoint",
)


def get_disk_usage(path: str = "/host") -> int:
    stats = os.statvfs(path)

    total = stats.f_blocks * stats.f_frsize
    available = stats.f_bavail * stats.f_frsize
    used = total - available

    if total == 0:
        return 0

    return round((used / total) * 100)


@app.get("/")
def disk_usage() -> dict[str, int]:
    return {"usage": get_disk_usage()}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}