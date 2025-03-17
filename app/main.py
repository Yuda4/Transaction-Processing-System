from fastapi import FastAPI, Request
from transactions import router
import uvicorn
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry, multiprocess
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI(title="Transaction Processing System")

# Create a custom registry
registry = CollectorRegistry()
multiprocess.MultiProcessCollector(registry)  # Enable multi-process mode (for Docker & Gunicorn)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"],
    registry=registry  # Use the custom registry
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Latency of HTTP requests",
    ["method", "endpoint"],
    registry=registry
)

# Middleware to track requests and response time
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        request_latency = time.time() - start_time

        REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
        REQUEST_LATENCY.labels(request.method, request.url.path).observe(request_latency)

        return response

# Add middleware
app.add_middleware(MetricsMiddleware)

# Expose Prometheus metrics endpoint
@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
