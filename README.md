# tiny-disk-usage

A tiny Python 3.12 HTTP service that reports the host filesystem usage as a percentage.
## Run it

```bash
docker compose up -d --build
```

Then:

```bash
curl http://localhost:8000/
```

Response:

```json
{"usage":73}
```

Health check:

```bash
curl http://localhost:8000/health
```

Response:

```json
{"status":"ok"}
```

## How the percentage is calculated

The service uses:

```python
total = stats.f_blocks * stats.f_frsize
available = stats.f_bavail * stats.f_frsize
used = total - available

usage = round((used / total) * 100)
```

`f_bavail` is used rather than simply `f_bfree`, which makes the result represent the space actually available to an unprivileged process.

The endpoint therefore gives you a simple integer from `0` to `100` representing the percentage of the host's `/` filesystem that is currently used.